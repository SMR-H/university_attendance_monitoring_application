from django.contrib import admin
from .models import Holiday
# Register your models here.
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin



class HolidayAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
	# show jalali date in list display 
	list_display = ['name', 'get_created_jalali']
	def get_created_jalali(self, obj):
		return date2jalali(obj.date).strftime('%Y/%m/%d ')
	
	get_created_jalali.short_description = 'تاریخ ایجاد'
	get_created_jalali.admin_order_field = 'date'

	# raw_id_fields = ('some_fields', )
	# readonly_fields = ('some_fields', 'date_field',)
	# you can override formfield, for example:
	# formfield_overrides = {
	#     JSONField: {'widget': JSONEditor},
	# }
	

admin.site.register(Holiday,HolidayAdmin)



