# from django.db.models import Q
import jdatetime
from django.core.management.base import BaseCommand

# Models
from course_holding.models import CourseHolding
from holiday.models import Holiday
from course_offering.models import CourseOffering
from course_status.models import CourseStatus

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        today_jalali = jdatetime.datetime.now().date()
        today_gregory = today_jalali.togregorian()

        is_holiday = Holiday.objects.filter(date=today_gregory).exists()
        if is_holiday:
            holiday = Holiday.objects.get(date=today_gregory)
            course_offerings = CourseOffering.objects.filter(semester_id__start_date__lte=today_gregory, semester_id__end_date__gte=today_gregory, weekday=today_gregory.strftime('%A').upper())
            
            for course_offering in course_offerings:
                holding = CourseHolding(
                    offered_course=course_offering,
                    course_status=CourseStatus.objects.create(status=CourseStatus.StatusChoices.OFFICIAL_HOLIDAY, description=holiday.name),
                    course_holding_type=CourseHolding.CourseHoldingTypeChoices.NORMAL,
                    class_id=course_offering.class_id,
                    date=today_gregory,
                    start_time=jdatetime.datetime.now().strftime("%H:%M:%S"),
                    end_time=course_offering.end_time,
                )
                holding.save()
        else:
            course_offerings = CourseOffering.objects.filter(semester_id__start_date__lte=today_gregory, semester_id__end_date__gte=today_gregory, weekday=today_gregory.strftime('%A').upper())
            
            for course_offering in course_offerings:
                holding = CourseHolding(
                    offered_course=course_offering,
                    course_status=CourseStatus.objects.create(),
                    course_holding_type=CourseHolding.CourseHoldingTypeChoices.NORMAL,
                    class_id=course_offering.class_id,
                    date=today_gregory,
                    start_time=jdatetime.datetime.now().strftime("%H:%M:%S"),
                    end_time=course_offering.end_time,
                )
                holding.save()
#---------------------------------------------------------
