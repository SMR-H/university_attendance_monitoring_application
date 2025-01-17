from django.db import models
import jdatetime
from university.models import University
from django.core.validators import MinValueValidator, MaxValueValidator
from validators.custom_validators import validate_semester_code


class Semester(models.Model):
    name = models.CharField(max_length=50, blank=True, editable=False)
    year = models.PositiveIntegerField(blank=True, editable=False, validators=[MinValueValidator(1390), MaxValueValidator(1420)])
    
    class SemesterTypeChoices(models.IntegerChoices):
        FIRST  = (1, 'نیمسال اول')
        SECOND = (2, 'نیمسال دوم')
        THIRD = (3,'تابستان')
    semester_type = models.IntegerField(choices=SemesterTypeChoices.choices)
    semester_code = models.PositiveSmallIntegerField(validators=[validate_semester_code])
    university_id = models.ForeignKey(University, on_delete= models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def semester_type_str(self):
        if self.semester_type == 1:
            return 'مهرماه'
        elif self.semester_type == 2:
            return 'بهمن ماه'
        elif self.semester_type == 3:
            return 'تابستان'

    def save(self, *args, **kwargs):
        jajali_date = jdatetime.date.fromgregorian(date=self.start_date)
        self.year = jajali_date.year
        self.name = str(self.year) + ' ' +  self.semester_type_str()
        super(Semester, self).save(*args, **kwargs)

    def __str__(self):
        return self.name