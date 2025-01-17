from django.db import models
from django.core.validators import MaxValueValidator

class CourseStatus(models.Model):
    class StatusChoices(models.TextChoices):
        WAITING = ('WAITING', 'Waiting')
        PRESENT = ('PRESENT', 'Present')
        ABSENT = ('ABSENT', 'Absent')
        OFFICIAL_HOLIDAY = ('OFFICIAL_HOLIDAY', 'Official holiday')
        UNEXPECTED_HOLIDAY = ('UNEXPECTED_HOLIDAY', 'Unexpected holiday')

    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.WAITING, max_length=20)   
    delay_amount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(60)])
    hurry_amount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(300)])
    description = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def has_delay(self):
        return self.delay_amount > 0

    def has_rush(self):
        return self.hurry_amount > 0

    def __str__(self):
        return self.status
    