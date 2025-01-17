from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.db import models
from university.models import University, Faculty
from major.models import Major
from validators.custom_validators import validate_username
from .custom_fields import CaseInsensitiveEmailField , CaseInsensitiveUsernameField


class User(AbstractUser):
    # username = CaseInsensitiveUsernameField(max_length=50, unique=True)
    username = CaseInsensitiveUsernameField(max_length=50, unique=True, validators=[validate_username])
    email = CaseInsensitiveEmailField(unique=True)
    class UserRoleChoices(models.TextChoices):
        UNIVERSITY= ('UNIVERSITY', 'رییس دانشگاه')
        FACULTY = ('FACULTY', 'رییس دانشکده')
        DEPARTMENT= ('DEPARTMENT', 'مدیر گروه')
        PROFESSOR= ('PROFESSOR', 'استاد')
        EMPLOYEE= ('EMPLOYEE', 'کارمند')
        MANAGER = ('MANAGER', 'آموزش')
        GENERAL_MANAGER = ('GENERAL_MANAGER', 'آموزش کل')
        ADMIN = ('ADMIN', 'ادمین')
    user_role = models.CharField(max_length=50, choices=UserRoleChoices.choices)
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    major_id = models.ManyToManyField(Major, blank=True)

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        else:
            return self.email
    
