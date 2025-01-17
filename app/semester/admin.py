from django.contrib import admin
from .models import Semester

from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
class SemesterAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name' , 'start_date_jalali','end_date_jalali']

    def start_date_jalali(self, obj):
        return date2jalali(obj.start_date).strftime('%Y/%m/%d ')
    start_date_jalali.short_description = 'تاریخ شروع ترم'

    def end_date_jalali(self, obj):
        return date2jalali(obj.end_date).strftime('%Y/%m/%d ')
    end_date_jalali.short_description = 'تاریخ پایان ترم'
    

admin.site.register(Semester,SemesterAdmin)