# Generated by Django 4.1.3 on 2023-04-17 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0003_rename_course_list_professor_course_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='course_id',
            new_name='allowed_course_id',
        ),
    ]
