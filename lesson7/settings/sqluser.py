import sqlite3


class User:
    def __init__(self, db_name, is_admin=False):
        self.__is_admin = is_admin
        self.__db_name = db_name

    def transaction(self, value):
        con = sqlite3.connect(self.__db_name)
        cur = con.cursor()
        ret = cur.execute(value).fetchall()
        con.commit()
        cur.close()
        con.close()
        return ret

    def get_students_list(self):
        query = 'SELECT * FROM students'
        students_query = self.transaction(query)

        return students_query

    def get_best_students_list(self):
        students_list_query = self.get_students_list()
        students_list = []
        query = f'SELECT id, first_name, last_name, group_id, FROM students ' \
                f'LEFT JOIN groups ON groups.id=students.id'
        for student in students_list_query:
            (student_id, first_name, last_name, group_id, ticket_id) = student
            query = f'SELECT avg(score) FROM grade WHERE ticket_id={ticket_id}'
            student_scores_list = self.transaction(query)
            students_list.append((first_name, last_name, round(student_scores_list[0][0], 2)))

        # sort students by score
        amount_of_students = len(students_list)
        for i in range(amount_of_students):
            for j in range(amount_of_students - 1):
                if students_list[j][2] < students_list[j + 1][2]:
                    buf = students_list[j]
                    students_list[j] = students_list[j + 1]
                    students_list[j + 1] = buf

        # 20% students best
        best_students_amount = round((amount_of_students * 20) / 100)
        best_students_list = []
        for i in range(best_students_amount):
            best_students_list.append(students_list[i])

        return best_students_list

    def get_student_info(self, ticket_id):
        if not self.is_student(ticket_id):
            print(f'get_student_info() ticket_id: {ticket_id} does not exists')
            return False
        query = f'SELECT students.id, first_name, last_name, groups.name, faculty.name FROM students ' \
                f'INNER JOIN groups ON groups.id=students.group_id ' \
                f'INNER JOIN faculty ON faculty.id=groups.faculty_id ' \
                f'WHERE ticket_id="{ticket_id}" '
        student_query = self.transaction(query)
        # print(student_query)

        (id_student, first_name, last_name, group, faculty) = student_query[0]
        print(f'student {id_student}: {first_name} {last_name} group: {group} faculty: {faculty}')
        return id_student, first_name, last_name, group, faculty

    def is_student(self, ticket_id):
        query = f'SELECT * FROM students WHERE ticket_id={ticket_id}'
        student_query = self.transaction(query)

        if len(student_query) == 0:
            return False
        else:
            return True

    # For Admin
    def add_student(self, first_name, last_name, faculty, group):
        if self.__is_admin:
            # check faculty
            if not self.is_faculty(faculty):
                print(f'Faculty: {faculty} does not exists')
                return False

            if not self.is_group(group):
                print(f'add_student() Group: {group} does not exists')
                return False

            query = f'SELECT id FROM faculty WHERE name="{faculty}"'
            faculty_query = self.transaction(query)
            if len(faculty_query) != 1:
                raise Exception('add_student() query faculty_id != 1')
            # faculty_id = faculty_query[0][0]
            # print('faculty_id: ', faculty_id)

            query = f'SELECT id FROM groups WHERE name="{group}"'
            group_query = self.transaction(query)
            if len(group_query) != 1:
                raise Exception('add_student() query ticket_id != 1')
            group_id = group_query[0][0]
            # print('group_id: ', group_id)

            # check duplicate
            query = f'SELECT * FROM students WHERE first_name="{first_name}" AND last_name="{last_name}" AND group_id="{group_id}"'
            is_student_query = self.transaction(query)
            # print(is_student_query)
            # print('is: ', len(is_student_query))
            if len(is_student_query) == 0:
                # before create new student ticket
                query = 'INSERT INTO tickets(id) VALUES(null)'
                self.transaction(query)
                query = 'SELECT max(id) FROM tickets'
                ticket_query = self.transaction(query)
                ticket_id = ticket_query[0][0]
                # get last value from tickets.id
                # print('st_id', ticket_id)
                query = f'INSERT INTO students(first_name, last_name, group_id, ticket_id) VALUES("{first_name}", "{last_name}", "{group_id}", {ticket_id})'
                self.transaction(query)
            else:
                print(f'add_student() student: {first_name} exists')
        else:
            print('You are not autorized to do this')
            return False

    def change_student(self, ticket_id, first_name, last_name, group):
        if not self.__is_admin:
            print('You are not autorized to do this')
            return False

        if self.is_student(ticket_id):
            print('student present')
            query = f'UPDATE students SET first_name="{first_name}", last_name="{last_name}", group_id="{group}" WHERE ticket_id="{ticket_id}"'
            self.transaction(query)
            return True

    def is_faculty(self, faculty):
        query = f'SELECT name FROM faculty WHERE name=\'{faculty}\''
        f = self.transaction(query)

        if not f:
            return False
        else:
            return True

    def add_faculty(self, faculty):
        if not self.is_faculty(faculty):
            value = f'INSERT INTO faculty(name) VALUES("{faculty}")'
            self.transaction(value)
            return True
        else:
            print(f'Faculty {faculty} exists')
            return False

    def is_group(self, group):
        query = f'SELECT name FROM groups WHERE name=\'{group}\''
        g = self.transaction(query)
        if not g:
            return False
        else:
            return True

    def add_group(self, group, faculty):
        if not self.__is_admin:
            print('You are not autorized to do this')
            return False

        if not self.is_group(group):
            if self.is_faculty(faculty):
                print('add group in faculty')
                query = f'SELECT id FROM faculty WHERE name=\'{faculty}\''
                faculty_query = self.transaction(query)
                if len(faculty_query) != 1:
                    raise Exception('function add_group, faculty != 1')
                faculty_id = faculty_query[0][0]
                query = f'INSERT INTO groups(name, faculty_id) VALUES("{group}", "{faculty_id}")'
                self.transaction(query)
            else:
                print(f'add_group(): Faculty {faculty} does not exists')
                return False
        else:
            print(f'add_group(): Group {group} exists')
            return False

    def add_grade(self, ticket_id, score):
        if not self.is_student(ticket_id):
            print(f'add_grade() ticket_id {ticket_id} does not exists')
            return False

        query = f'INSERT INTO grade(score, ticket_id) VALUES("{score}", "{ticket_id}")'
        self.transaction(query)
        return True

