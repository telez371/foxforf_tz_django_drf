from rest_framework import serializers
from .models import Course
from teacher.serializers import TeacherSerializer

class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'teachers', 'students']


