from rest_framework import viewsets, permissions
from teacher.models import Teacher
from teacher.serializers import TeacherSerializer



class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
