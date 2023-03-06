from django.contrib import admin
from .models import Teacher, Course, Webinar, Salary, Student


@admin.register(Student)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'photo', 'first_name', 'last_name', 'bio',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'photo', 'first_name', 'last_name', 'bio', 'course')


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'start_time', 'language', 'status')
    filter_horizontal = ('teachers', 'students')
    list_filter = ('status',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'file', 'link', 'text')


@admin.register(Salary)
class TeacherSalaryAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'hourly_rate', 'hours_worked', 'total_salary')
    list_filter = ('teacher',)
