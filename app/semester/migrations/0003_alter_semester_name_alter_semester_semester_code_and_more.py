# Generated by Django 4.1.3 on 2023-03-16 20:20

import django.core.validators
from django.db import migrations, models
import validators.custom_validators


class Migration(migrations.Migration):

    dependencies = [
        ('semester', '0002_semester_university_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_code',
            field=models.PositiveSmallIntegerField(validators=[validators.custom_validators.validate_semester_code]),
        ),
        migrations.AlterField(
            model_name='semester',
            name='year',
            field=models.PositiveIntegerField(blank=True, editable=False, validators=[django.core.validators.MinValueValidator(1390), django.core.validators.MaxValueValidator(1420)]),
        ),
    ]
