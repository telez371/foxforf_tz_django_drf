from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.ImageField(upload_to='materials', blank=True)
    link = models.URLField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='teachers', blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='students', blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Webinar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='webinars')
    start_time = models.DateTimeField()

    language_choices = [
        ('Русский', 'Русский'),
        ('Английский', 'Английский'),
    ]
    language = models.CharField(max_length=20, choices=language_choices, default='russian')

    status_choices = [
        ('Создан', 'Создан'),
        ('Сейчас идет', 'Сейчас идет'),
        ('Закончен', 'Закончен'),
        ('Отменен', 'Отменен')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='created')
    teachers = models.ManyToManyField(Teacher, related_name='webinars')
    students = models.ManyToManyField(Student, related_name='webinars_registered', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Webinars"
        ordering = ['start_time']


class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=10, decimal_places=2)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.teacher
