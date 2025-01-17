from django.db import models
from course.models import Course
from professor.models import Professor
from semester.models import Semester
from classroom.models import Classroom
from major.models import Major

from validators.custom_validators import validate_only_digits


class CourseOffering(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor_id = models.ManyToManyField(Professor)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class WeekdayChoices(models.TextChoices):
        SATURDAY = ('SATURDAY', 'شنبه')
        SUNDAY = ('SUNDAY', 'یکشنبه')
        MONDAY = ('MONDAY', 'دوشنبه')
        TUESDAY = ('TUESDAY', 'سه شنبه')
        WEDNESDAY = ('WEDNESDAY', 'چهارشنبه')
        THURSDAY = ('THURSDAY', 'پنج شنبه')
        FRIDAY = ('FRIDAY', 'جمعه')

    weekday = models.CharField(max_length=20, choices=WeekdayChoices.choices)

    start_time = models.TimeField()
    end_time = models.TimeField()
    offering_course_code = models.CharField(max_length=50, validators=[validate_only_digits], unique=True)
    major_id = models.ManyToManyField(Major)
    aggregate = models.BooleanField(default=False)

    class GenderChoices(models.TextChoices):
        BOTH = ('BOTH', 'فرقی ندارد')
        MALE = ('MALE', 'مرد')
        FEMALE = ('FEMALE', 'زن')

    course_gender = models.CharField(max_length=20, choices=GenderChoices.choices)

    def __str__(self):
        return self.course_id.name


class CourseOfferingFile(models.Model):
    name = models.CharField(max_length=250)
    file = models.FileField(upload_to='files/')
    upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
