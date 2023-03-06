from django.contrib import admin
from course.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'file', 'link', 'text')


