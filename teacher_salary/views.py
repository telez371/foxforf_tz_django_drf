from rest_framework import viewsets, permissions
from teacher_salary.models import Salary
from webinar.serializers import WebinarSerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = WebinarSerializer
    permission_classes = [permissions.IsAuthenticated]
