from rest_framework import viewsets, permissions
from django.utils import timezone
from webinar.models import Webinar
from webinar.serializers import WebinarSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from decimal import Decimal


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
