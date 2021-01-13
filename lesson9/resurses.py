import json
from flask_restful import Resource, Api, request
from models.models import *


class StudentsResources(Resource):
    def get(self, student_id=None):
        if student_id:
            student = Students.objects.get(id=student_id)
            return json.loads(student.to_json())
        else:
            student = Students.objects()
            return json.loads(student.to_json())

    def post(self):
        first_name = request.json.get('first_name')
        second_name = request.json.get('second_name')
        sure_name = request.json.get('sure_name')
        first_name_couch = request.json.get('first_name_couch')
        second_name_couch = request.json.get('second_name_couch')
        sure_name_couch = request.json.get('sure_name_couch')
        faculty = request.json.get('faculty')
        group = request.json.get('group')
        # couch = request.json.get('couch')
        marks = request.json.get('marks')

        student = Students()

        student.faculty = faculty
        student.group = group
        # student.couch = couch
        student.marks = marks

        student.couch = Name(
            first_name=first_name_couch,
            second_name=second_name_couch,
            sure_name=sure_name_couch
        )

        student.name = Name(
            first_name=first_name,
            second_name=second_name,
            sure_name=sure_name
        )

        student.save()

        return {'Success': 'student was created'}


    def delete(self, student_id):
        student = Students.objects(id=student_id)

        if student:
            student.delete()

            return {'Success': f'student was deleted {student_id}'}
        else:
            return  {'Error': f'student not found {student_id}'}

    def put(self, student_id):
        student = Students.objects(id=student_id).first()
        if student:
            first_name = request.json.get('first_name')
            second_name = request.json.get('second_name')
            sure_name = request.json.get('sure_name')
            first_name_couch = request.json.get('first_name_couch')
            second_name_couch = request.json.get('second_name_couch')
            sure_name_couch = request.json.get('sure_name_couch')
            faculty = request.json.get('faculty')
            group = request.json.get('group')
            marks = request.json.get('marks')

            if first_name:
                student.name.first_name = second_name
            if second_name:
                student.name.second_name = second_name
            if sure_name:
                student.name.sure_name = sure_name

            if first_name_couch:
                student.couch.first_name = first_name_couch
            if second_name_couch:
                student.couch.second_name = second_name_couch
            if sure_name_couch:
                student.couch.sure_name = sure_name_couch

            if faculty:
                student.faculty = faculty
            if group:
                student.group = group
            if marks:
                student.marks = marks

            student.save()
            return {'Success': f'student was updated {student_id}'}
        else:
            return {'Error': f'student not found {student_id}'}