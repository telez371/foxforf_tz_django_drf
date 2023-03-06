from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from course.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from decimal import Decimal
from django.utils import timezone



class StudentlistPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseProfileViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().values_list('name', 'description', 'teachers')
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = Webinar.objects.all()
    serializer_class = WebinarSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def update_salary(self, request, pk=None):
        webinar = self.get_object()
        current_time = timezone.now()
        status = request.data.get('status')
        teacher = request.data.get('teacher')

        if status == 'Создан' and teacher:
            webinar.created_time = current_time
            webinar.save()
            return Response({'message': 'Webinar created time saved.'})

        elif status == 'Закончен':

            start_time = webinar.created_time
            time_diff = (current_time - start_time).total_seconds() / 3600
            hourly_rate = webinar.teachers.filter(pk=teacher).first().salary.hourly_rate
            salary = Decimal(time_diff * hourly_rate)

            teacher_salary = teacher.salary
            teacher_salary.total_salary = salary
            teacher_salary.save()

            return Response({'message': f'Teacher salary updated: {salary}.'})

        return Response({'message': 'Invalid request.'})


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = WebinarSerializer
    permission_classes = [permissions.IsAuthenticated]
