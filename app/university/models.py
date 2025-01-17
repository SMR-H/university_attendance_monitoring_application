from django.db import models
from validators.custom_validators import validate_only_digits
from location.models import City

class University(models.Model):
    name = models.CharField(max_length=250, verbose_name='واحد (دانشگاه)')
    university_code = models.CharField(max_length=50, validators=[validate_only_digits], unique=True)
    city_id = models.ForeignKey(City , on_delete=models.CASCADE, verbose_name='شهر')
    def __str__(self):
        return self.name    

class Faculty(models.Model):
    name = models.CharField(max_length=250, verbose_name='دانشکده')
    faculty_code = models.CharField(max_length=50, validators=[validate_only_digits])
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name='واحد (دانشگاه)')
    class Meta:
        unique_together = ('faculty_code', 'university_id')
    def __str__(self):
        return f'{self.name} / {self.university_id.name}'

class Department(models.Model):
    name = models.CharField(max_length=250, verbose_name='گروه')
    department_code = models.CharField(max_length=50, validators=[validate_only_digits], unique=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE,verbose_name='دانشکده / دانشگاه')
    def __str__(self):
        return f'{self.name} - {self.faculty_id.name} - {self.faculty_id.university_id.name}'
