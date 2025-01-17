from django.db import models
from validators.custom_validators import validate_only_digits
from course.models import Course
from account.models import User
# Create your models here.

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    professor_code = models.CharField(max_length=50,unique=True, validators=[validate_only_digits])
    is_active = models.BooleanField(default=True)
    allowed_course_id = models.ManyToManyField(Course)

    class GenderChoices(models.TextChoices):
        MALE = ('MALE', 'مرد')
        FEMALE = ('FEMALE', 'زن')

    gender = models.CharField(max_length=20,choices=GenderChoices.choices)
    def __str__(self):
        return self.user.get_full_name()

