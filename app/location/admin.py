from django.contrib import admin
from .models import Province,City
# Register your models here.
class ProvinceAdmin(admin.ModelAdmin):
    list_display= ['name', 'province_code']
    ordering = ('province_code',)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'province_id']
    search_fields = ['province_id__name']

admin.site.register(Province,ProvinceAdmin)
admin.site.register(City,CityAdmin)