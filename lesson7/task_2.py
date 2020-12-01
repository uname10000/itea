import sqlite3
import random
from settings.settings import Settings
from settings.sqluser import User


def generate_data(s, admin):
    for faculty, groups in s.faculty.items():
        admin.add_faculty(faculty)
        for group in groups:
            admin.add_group(group, faculty)

    for st in s.students:
        (first_name, last_name, faculty, group) = st
        admin.add_student(first_name, last_name, faculty, group)

    students_list = admin.get_students_list()
    for student in students_list:
        (student_id, first_name, last_name, group, ticket_id) = student
        for i in range(10):
            score = random.randint(2, 5)
            admin.add_grade(ticket_id, score)


def install_db(settings):
    conn = sqlite3.connect(settings.db_name)
    cur = conn.cursor()

    cur.execute(settings.create_student_table)
    cur.execute(settings.create_ticket_table)
    cur.execute(settings.create_faculty_table)
    cur.execute(settings.create_group_table)
    cur.execute(settings.create_grade_table)

    conn.commit()
    cur.close()
    conn.close()


settings = Settings()
user = User(settings.db_name)
admin = User(settings.db_name, True)

install_db(settings)
generate_data(settings, admin)
print('-'*20)


admin.change_student(9, 'Mimi', 'M', 1)
admin.get_student_info(9)
admin.add_grade(9, 5)
best_students_list = admin.get_best_students_list()

for student in best_students_list:
    (first_name, last_name, average_score) = student
    print(f'Name: {first_name} {last_name} average score: {average_score}')



