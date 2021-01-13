import random

from models.models import *
from settings import *

me.connect('lesson_9')

settings = Settings()

for i in range(100):
    first_name_student_index = random.randrange(0, len(settings.valid_first_name))
    second_name_student_index = random.randrange(0, len(settings.valid_second_name))
    sure_name_student_index = random.randrange(0, len(settings.valid_sure_name))

    first_name_couch_index = random.randrange(0, len(settings.valid_first_name))
    second_name_couch_index = random.randrange(0, len(settings.valid_second_name))
    sure_name_couch_index = random.randrange(0, len(settings.valid_sure_name))

    faculty_index = random.randrange(0, len(settings.valid_faculty))
    group_index = random.randrange(0, len(settings.valid_group))

    student = Students()
    student.name = Name()
    student.couch = Name()

    student.name.first_name = settings.valid_first_name[first_name_student_index]
    student.name.second_name = settings.valid_second_name[second_name_student_index]
    student.name.sure_name = settings.valid_sure_name[sure_name_student_index]

    student.couch.first_name = settings.valid_first_name[first_name_couch_index]
    student.couch.second_name = settings.valid_second_name[second_name_couch_index]
    student.couch.sure_name = settings.valid_sure_name[sure_name_couch_index]

    student.faculty = settings.valid_faculty[faculty_index]
    student.group = settings.valid_group[group_index]

    # У каждого студента по 20 оценок
    for j in range(20):
        mark_index = random.randrange(0, len(settings.valid_marks))
        student.marks.append(int(settings.valid_marks[mark_index]))

    student.save()
