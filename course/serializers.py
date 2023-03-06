from rest_framework import serializers
from .models import Student, Teacher, Course, Webinar, Salary


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user_profile', 'photo', 'bio']


#
#
class TeacherSerializer(serializers.ModelSerializer):
    user_profile = Teacher

    class Meta:
        model = Teacher
        fields = ('id', 'user_profile', 'photo', 'bio', 'course')


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'teachers', 'students']


class WebinarSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    students = StudentProfileSerializer(many=True)

    class Meta:
        model = Webinar
        fields = '__all__'


#


class SalarySerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())

    class Meta:
        model = Salary
        fields = ['id', 'teacher', 'hourly_rate', 'hours_worked', 'total_salary']
        read_only_fields = ['hours_worked', 'total_salary']
