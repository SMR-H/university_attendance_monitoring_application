from django.contrib import admin
from .models import CourseOffering, CourseOfferingFile
# Register your models here.

class CourseOfferingAdmin(admin.ModelAdmin):
    filter_horizontal = ('professor_id','major_id')
    # filter_vertical = ('professor_id',)
    list_display = ['offerd_course_name',  'semester_id', 'university_name','display_professors', 'start_time', 'end_time', 'weekday','display_majors']
    
    def offerd_course_name(self,obj):
        return obj.course_id.name
    def university_name(self,obj):
        return obj.class_id.faculty_id.university_id.name
    
    def display_professors(self, obj):
        return "، ".join([professor.user.get_full_name() for professor in obj.professor_id.all()])
    display_professors.short_description = 'Professor'

    def display_majors(self, obj):
        return " | ".join([major.__str__() for major in obj.major_id.all()])
    display_majors.short_description = 'Major'    


admin.site.register(CourseOffering,CourseOfferingAdmin)
admin.site.register(CourseOfferingFile)