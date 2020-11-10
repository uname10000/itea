from datetime import datetime, timedelta
from abc import ABC, abstractmethod


class Person:
    def __init__(self, surname, birth_date, faculty):
        self.surname = surname
        self.birth_date = birth_date
        self.faculty = faculty

    def age(self):
        today = datetime.now()
        return today.year - self.birth_date.year

    @abstractmethod
    def show_info(self):
        pass


class Entrant(Person):
    def __init__(self, surname, birth_date, faculty):
        super().__init__(surname, birth_date, faculty)

    def show_info(self):
        print(f'surname: {self.surname}')
        print(f'birth_date: {self.birth_date}')
        print(f'faculty: {self.faculty}')
        print(f'age: {self.age()}')


class Student(Person):
    def __init__(self, surname, birth_date, faculty, course):
        super().__init__(surname, birth_date, faculty)
        self.course = course

    def show_info(self):
        print(f'surname: {self.surname}')
        print(f'birth_date: {self.birth_date}')
        print(f'faculty: {self.faculty}')
        print(f'course: {self.course}')
        print(f'age: {self.age()}')


class Teacher(Person):
    def __init__(self, surname, birth_date, faculty, position, experience):
        super().__init__(surname, birth_date, faculty)
        self.position = position
        self.experience = experience

    def show_info(self):
        print(f'surname: {self.surname}')
        print(f'birth_date: {self.birth_date}')
        print(f'faculty: {self.faculty}')
        print(f'position: {self.position}')
        print(f'experience: {self.experience}')
        print(f'age: {self.age()}')


def show_info(persons):
    for person in persons:
        person.show_info()
        print('-'*40)
# entrant1 = Entrant('entrant1', datetime(2000, 10, 1), 'Mathematics')
# student1 = Student('student1', datetime(2004, 10, 1), 'Biology', 4)
# teacher1 = Teacher('student1', datetime(1970, 10, 1), 'Biology', 'Professor', 15)
# print(f'entrant age: {entrant1.age()}')
# print(f'student age: {student1.age()}')
# print(f'teacher age: {teacher1.age()}')
# print('-'*40)
#
# entrant1.show_info()
# print('-'*40)
# student1.show_info()
# print('-'*40)
# teacher1.show_info()

persons = list()

persons.append(Entrant('entrant1', datetime(2000, 3, 10), 'Mathematics'))
persons.append(Entrant('entrant2', datetime(1999, 6, 5), 'Economy'))
persons.append(Entrant('entrant3', datetime(2001, 4, 7), 'Mathematics'))
persons.append(Entrant('entrant4', datetime(2002, 8, 6), 'Mathematics'))
persons.append(Entrant('entrant5', datetime(2000, 10, 2), 'Mathematics'))

persons.append(Student('student1', datetime(2003, 1, 1), 'Biology', 4))
persons.append(Student('student3', datetime(2006, 6, 4), 'Mathematics', 4))
persons.append(Student('student4', datetime(2008, 3, 11), 'Mathematics', 5))
persons.append(Student('student5', datetime(2009, 2, 10), 'Biology', 1))

persons.append(Teacher('teacher1', datetime(1970, 7, 10), 'Economy', 'Professor', 15))
persons.append(Teacher('teacher2', datetime(1971, 12, 3), 'Biology', 'Professor', 12))
persons.append(Teacher('teacher3', datetime(1975, 3, 24), 'Economy', 'Teacher', 5))
persons.append(Teacher('teacher4', datetime(1973, 9, 26), 'Biology', 'Professor', 11))
persons.append(Teacher('teacher5', datetime(1972, 10, 15), 'Mathematics', 'Teacher', 6))

show_info(persons)


while True:
    print('Type Exit to exit')
    text = input('Enter age1> ')
    if text == 'exit':
        break
    age_1 = int(text)
    text = input('Enter age2> ')
    if text == 'exit':
        break
    age_2 = int(text)

    if age_1 > age_2:
        print('age1 must be les or equal than age2')
        continue

    for person in persons:
        if (person.age() >= age_1) and (person.age() <= age_2):
            person.show_info()
            print('-'*40)
