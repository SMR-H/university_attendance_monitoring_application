# Generated by Django 4.1.3 on 2023-03-16 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_offering', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseoffering',
            old_name='day',
            new_name='weekday',
        ),
    ]
