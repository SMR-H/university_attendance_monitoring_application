from django.db import models
from course_offering.models import CourseOffering
from course_status.models import CourseStatus
from professor.models import Professor
from classroom.models import Classroom

class CourseHolding(models.Model):
    offered_course = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    course_status = models.OneToOneField(CourseStatus, on_delete=models.CASCADE)
    class CourseHoldingTypeChoices(models.TextChoices):
        NORMAL = ('NORMAL', 'عادی')
        MAKEUP = ('MAKEUP', 'جبرانی')
        EXTRA = ('EXTRA', 'کلاس اضافه')
    course_holding_type = models.CharField(max_length=20, choices=CourseHoldingTypeChoices.choices)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE,null=True, blank=True)
    class_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()




# def save(self, *args, **kwargs):
#     if self.course_holding_type == 'normal':
#         self.class_id = self.offered_course.class_id
#     super(CourseHolding, self).save(*args, **kwargs)

