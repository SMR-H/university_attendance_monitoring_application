# Generated by Django 4.1.3 on 2023-04-01 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_holding', '0003_rename_professor_courseholding_professor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseholding',
            name='weekday',
        ),
    ]
