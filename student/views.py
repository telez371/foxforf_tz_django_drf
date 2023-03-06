from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from student.models import Student
from student.serializers import StudentProfileSerializer


class StudentlistPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
