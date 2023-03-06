from django.contrib import admin
from student.models import Student


@admin.register(Student)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'photo', 'first_name', 'last_name', 'bio',)
