from django.db import models
from university.models import Faculty
from django.core.validators import MaxValueValidator


class Classroom(models.Model):
    class_number = models.PositiveIntegerField(validators=[MaxValueValidator(1000000)])
    floor = models.PositiveSmallIntegerField(validators=[MaxValueValidator(20)])
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.class_number} - {self.faculty_id.university_id.name} - {self.faculty_id.name}'