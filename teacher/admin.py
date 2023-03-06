from django.contrib import admin
from teacher.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'photo', 'first_name', 'last_name', 'bio', 'course')
