from django.contrib import admin
from .models import  University,Faculty,Department
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display= ['name','faculty_id']


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty_code', 'university_id']
    

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'city_id', 'province_id']
    def province_id(self, obj):
        return obj.city_id.province_id
    province_id.short_description = 'استان'
    search_fields = ['city_id__name']

admin.site.register(University,UniversityAdmin)
admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)