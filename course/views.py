from rest_framework import viewsets, permissions
from course.models import Course
from teacher.serializers import TeacherSerializer


class CourseProfileViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().values_list('name', 'description', 'teachers')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

