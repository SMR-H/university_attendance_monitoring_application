from django.db import models
from validators.custom_validators import validate_only_digits
from university.models import Department
# Create your models here.
class Degree(models.Model):
    name = models.CharField(max_length=250)
    degree_code = models.PositiveIntegerField(unique=True)
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=250)
    group_code = models.PositiveIntegerField(unique=True)
    def __str__(self):
        return self.name

class MajorList(models.Model):
    name = models.CharField(max_length=250)
    major_code = models.CharField(max_length=50, validators=[validate_only_digits], unique=True)
    degree_id = models.ForeignKey(Degree, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} - {self.degree_id.name}'
    
class Major(models.Model):
    major_id = models.ForeignKey(MajorList, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('major_id', 'department_id')

    def __str__(self):
        return f'{self.major_id.name} - {self.major_id.degree_id.name} - {self.department_id.faculty_id.university_id.name}'