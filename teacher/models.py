from django.db import models
from django.contrib.auth.models import User
from course.models import Course


class Teacher(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='teachers', blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
