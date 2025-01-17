from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display =['name', 'course_code', 'course_type', 'theoretical_credit', 'practical_credit']
    
admin.site.register(Course, CourseAdmin)