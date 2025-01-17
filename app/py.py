# from datetime import datetime

# # Get the current date and time
# now = datetime.now()

# # Get the name of the day of the week (e.g. "Monday", "Tuesday", etc.)
# day_of_week = now.strftime("%A %T %Y")

# # Print the name of the day of the week
# print("Today is", day_of_week)

import jdatetime

# # Get the current Jalali date
# now = jdatetime.datetime.now()

# # Get the name of the day of the week in Persian
# day_of_week = now.strftime("%A %H:%M %Y")

# # Print the name of the day of the week
# print("Today is", day_of_week)

###################
today_jalali = jdatetime.datetime.now().date()
today_gregory = today_jalali.togregorian()
print(today_gregory.strftime('%A').upper())
#--------------------------------------------------------
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        today_jalali = jdatetime.datetime.now().date()
        today_gregory = today_jalali.togregorian()
        print(today_gregory)

        is_holiday = Holiday.objects.filter(date=today_gregory).exists()
        if is_holiday:
            holiday = Holiday.objects.get(date=today_gregory)
            course_status = CourseStatus.objects.create(state=CourseStatus.State.OFFICIAL_HOLIDAY, description=holiday.name)
            holding = CourseHolding(
                offered_course=None,
                course_status=course_status,
                course_holding_type=CourseHolding.CourseHoldingType.NORMAL,
                class_id=None,
                date=today_gregory,
                start_time=jdatetime.datetime.now().strftime("%H:%M:%S"),
                end_time=None,
            )
            holding.save()
        else:
            course_offerings = CourseOffering.objects.filter(semester_id__start_date__lte=today_gregory, semester_id__end_date__gte=today_gregory, weekday=today_gregory.strftime('%A').upper())
            for course_offering in course_offerings:
                # create a new CourseHolding record for this offering
                holding = CourseHolding(
                    offered_course=course_offering,
                    course_status=CourseStatus.objects.create(),
                    course_holding_type=CourseHolding.CourseHoldingType.NORMAL,
                    class_id=course_offering.class_id,
                    date=today_gregory,
                    start_time=jdatetime.datetime.now().strftime("%H:%M:%S"),
                    end_time=course_offering.end_time,
                )
                holding.save()
########################
# لطفا یکی از مقادیر
# "بله) "TRUE"
# "خیر" "FALSE"
# را برای وضعیت مجتمع سازی هر درس انتخاب کنید
# "987_684_654"