from django.contrib import admin
from course_holding.models import CourseHolding

class CourseHoldingAdmin(admin.ModelAdmin):
    list_display = ['offered_course', 'course_status','course_holding_type','class_id','date','start_time','end_time']
    def offered_course(self,obj):
        return obj.offered_course.course_id.name
    


admin.site.register(CourseHolding,CourseHoldingAdmin)