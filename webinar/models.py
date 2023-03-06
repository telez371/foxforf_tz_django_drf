from django.db import models
from course.models import Course
from student.models import Student
from teacher.models import Teacher



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


