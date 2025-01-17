from django.contrib import admin
from .models import Major,MajorList,Degree,Group
# Register your models here.

class MajorListAdmin(admin.ModelAdmin):
    list_display= ['name', 'degree_id']
    
class MajorAdmin(admin.ModelAdmin):
    list_display=['major_id', 'university_id']

    def university_id(self,obj):
        return f'{obj.department_id.name} - {obj.department_id.faculty_id.name} - {obj.department_id.faculty_id.university_id.name}'
    university_id.short_description = 'گروه - دانشکده - دانشگاه'

admin.site.register(MajorList, MajorListAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Degree)
admin.site.register(Group)