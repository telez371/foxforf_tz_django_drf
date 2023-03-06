from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.ImageField(upload_to='materials', blank=True)
    link = models.URLField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name

