from django.contrib import admin
from teacher_salary.models import Salary


@admin.register(Salary)
class TeacherSalaryAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'hourly_rate', 'hours_worked', 'total_salary')
    list_filter = ('teacher',)