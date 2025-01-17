from django.db import models
from django.core.validators import MaxValueValidator
from validators.custom_validators import validate_only_digits
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=250)
    course_code = models.CharField(max_length=50, validators=[validate_only_digits], unique=True)
# TODO: bayad course_type eslah she (maghadiri ke toye database zakhere mishan bayad english bashan) / behtare az model.textchoice estfade konam
    COURSE_TYPE = [
    ('جبراني', 'جبراني'),
    ('اختياري', 'اختياري'),
    ('علوم وابسته دانشكده اي', 'علوم وابسته دانشكده اي'),
    ('عمومي', 'عمومي'),
    ('پايه', 'پايه'),
    ('اصلي', 'اصلي'),
    ('تخصصي', 'تخصصي'),
    ('پيش دانشگاهي', 'پيش دانشگاهي'),
    ('علوم پايه اختصاصي', 'علوم پايه اختصاصي'),
    ('علوم پايه مشترك', 'علوم پايه مشترك'),
    ('صلاحيت مدرسي', 'صلاحيت مدرسي'),
    ('علوم وابسته بيمارستاني', 'علوم وابسته بيمارستاني'),
    ('الزامي', 'الزامي'),
    ('پروژه/پایان نامه/رساله', 'پروژه/پایان نامه/رساله'),
    ('مهارت هاي عملي', 'مهارت هاي عملي'),
    ('سمينار', 'سمينار'),
    ('کاروزي', 'کاروزي'),
    ('کارآموزي در عرصه', 'کارآموزي در عرصه'),
    ('کلینیکی', 'کلینیکی')]

    course_type = models.CharField(max_length=50, choices=COURSE_TYPE)
    theoretical_credit = models.PositiveSmallIntegerField(validators=[MaxValueValidator(25)])
    practical_credit = models.PositiveSmallIntegerField(validators=[MaxValueValidator(25)])
    def __str__(self):
        return self.name