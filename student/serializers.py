from rest_framework import serializers
from student.models import Student


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user_profile', 'photo', 'bio']