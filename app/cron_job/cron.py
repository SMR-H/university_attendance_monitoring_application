
####! ---------toye course-offering management/commands -------!#######

# from django.db.models import Q
# import jdatetime
# # Models

# from course_holding.models import CourseHolding
# from course_offering.models import CourseOffering
# from course_status.models import CourseStatus

# def create_course_holdings_cron_job():
#     today_jalali = jdatetime.datetime.now().date()
#     today_gregory = today_jalali.togregorian()
#     course_offerings = CourseOffering.objects.filter(semester_id__start_date__lte=today_gregory, semester_id__end_date__gte=today_gregory, weekday=today_gregory.strftime('%A').upper())
#     for course_offering in course_offerings:
#         # create a new CourseHolding record for this offering
#         holding = CourseHolding(
#             offered_course=course_offering,
#             course_status=CourseStatus.objects.create(),
#             course_holding_type=CourseHolding.CourseHoldingType.NORMAL,
#             class_id=course_offering.class_id,
#             date=today_gregory,
#             start_time=course_offering.start_time,
#             end_time=course_offering.end_time,
#         )
#         holding.save()




####################################
# import jdatetime
# from django_cron import CronJobBase, Schedule
# # Models
# from course_offering.models import CourseOffering
# from course_holding.models import CourseHolding
# from course_status.models import CourseStatus
# from semester.models import Semester

# class CreateCourseHoldingsCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1440  # once per day

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'myapp.create_course_holdings_cron_job'    # a unique code for this cron job

#     def do(self):
#         today_jalali = jdatetime.datetime.now().date()
#         today_gregory = today_jalali.togregorian()
#         semesters = Semester.objects.all()
#         for semester in semesters:
#             if today_gregory >= semester.start_date and today_gregory <= semester.end_date:
#                 course_offerings = CourseOffering.objects.filter(semester_id=semester, weekday=today_gregory)
#         for course_offering in course_offerings:
#             # create a new CourseHolding record for this offering
#             holding = CourseHolding(
#                 offered_course=course_offering,
#                 course_status=CourseStatus.objects.create(),
#                 course_holding_type=CourseHolding.CourseHoldingType.NORMAL,
#                 class_id=course_offering.class_id,
#                 date=today_gregory,
#                 start_time=course_offering.start_time,
#                 end_time=course_offering.end_time,
#             )
#             holding.save()