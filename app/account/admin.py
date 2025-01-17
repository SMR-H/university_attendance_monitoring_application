from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['username', 'full_name', 'email', 'user_role', 'id','university_id', 'is_superuser', 'is_active']
    exclude = ['groups','user_permissions']
    def full_name(self, obj):
        return obj.get_full_name()

        
admin.site.register(User,UserAdmin)
