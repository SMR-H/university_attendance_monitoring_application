from django.contrib import admin
from .models import Classroom

class ClassroomAdmin(admin.ModelAdmin):
    list_display=['class_number', 'floor', 'faculty_name', 'university_name']

    def faculty_name(self,obj):
        return obj.faculty_id.name

    def university_name(self,obj):
        return obj.faculty_id.university_id.name

admin.site.register(Classroom,ClassroomAdmin)