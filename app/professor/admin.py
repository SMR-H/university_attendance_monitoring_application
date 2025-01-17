from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display=['user','university_id','professor_code', 'is_active']
    def university_id(self,obj):
        return obj.user.university_id


admin.site.register(Professor,ProfessorAdmin)