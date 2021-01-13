import mongoengine as me


class Name(me.EmbeddedDocument):
    first_name = me.StringField()
    second_name = me.StringField()
    sure_name = me.StringField()


class Students(me.Document):
    name = me.EmbeddedDocumentField(Name)
    faculty = me.StringField()
    group = me.StringField()
    couch = me.EmbeddedDocumentField(Name)
    marks = me.ListField(me.IntField())

    @classmethod
    def get_best_students(cls, faculty):
        students = cls.objects(faculty=faculty)

        list_of_best_students = []

        for student in students:
            is_best_student = True
            for mark in student.marks:
                if mark != 5:
                    is_best_student = False
                    break

            if is_best_student:
                list_of_best_students.append(student)

        return list_of_best_students



    @classmethod
    def get_students_curator(cls, first_curator_name, second_curator_name, sure_curator_name):
        students = cls.objects()

        list_of_students = []

        for student in students:
            if student.couch.first_name == first_curator_name and \
                student.couch.second_name == second_curator_name and \
                student.couch.sure_name == sure_curator_name:
                list_of_students.append(student)

        return list_of_students
