from rest_framework import serializers
from teacher.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user_profile = Teacher
    class Meta:
        model = Teacher
        fields = ('id', 'user_profile', 'photo', 'bio', 'course')