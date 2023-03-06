from rest_framework import serializers
from student.serializers import StudentProfileSerializer
from teacher.serializers import TeacherSerializer
from webinar.models import Webinar


class WebinarSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    students = StudentProfileSerializer(many=True)

    class Meta:
        model = Webinar
        fields = '__all__'


