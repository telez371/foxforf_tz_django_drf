from django.contrib import admin
from webinar.models import Webinar



@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'start_time', 'language', 'status')
    filter_horizontal = ('teachers', 'students')
    list_filter = ('status',)
