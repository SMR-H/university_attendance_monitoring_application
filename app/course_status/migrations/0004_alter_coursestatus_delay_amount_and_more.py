# Generated by Django 4.1.3 on 2023-04-17 04:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_status', '0003_remove_coursestatus_state_coursestatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestatus',
            name='delay_amount',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(60)]),
        ),
        migrations.AlterField(
            model_name='coursestatus',
            name='hurry_amount',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(300)]),
        ),
    ]
