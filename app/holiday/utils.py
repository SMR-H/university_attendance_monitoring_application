from .models import  Holiday

def is_holiday(date):
    try:
        Holiday.objects.get(holiday_date=date)
        return True
    except Holiday.DoesNotExist:
        return False