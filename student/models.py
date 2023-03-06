from django.contrib.auth.models import User
from django.db import models



class Student(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='students', blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
