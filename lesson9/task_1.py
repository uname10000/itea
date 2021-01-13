from models.models import *

me.connect('lesson_9')

students = Students.get_best_students('faculty 3')

for student in students:
    print(f'first_name: {student.name.first_name}')
    print(f'second_name: {student.name.second_name}')
    print(f'sur_name: {student.name.sure_name}')
    print('-'*20)
    print(f'first_name_couch: {student.couch.first_name}')
    print(f'second_name_couch: {student.couch.second_name}')
    print(f'sure_name_couch: {student.couch.sure_name}')
    print('-' * 20)
    print(f'faculty: {student.faculty}')
    print(f'group: {student.group}')

    marks = []
    for mark in student.marks:
        marks.append(mark)

    print(f'marks: {marks}')

    print('#'*20)


print()

couch_first_name = 'Yaroslav'
couch_second_name = 'Rostislavovich'
couch_sure_name = 'Alenovich'

students = Students.get_students_curator(couch_first_name, couch_second_name, couch_sure_name)

for student in students:
    print(f'first_name: {student.name.first_name}')
    print(f'second_name: {student.name.second_name}')
    print(f'sur_name: {student.name.sure_name}')
    print('-'*20)
    print(f'first_name_couch: {student.couch.first_name}')
    print(f'second_name_couch: {student.couch.second_name}')
    print(f'sure_name_couch: {student.couch.sure_name}')

