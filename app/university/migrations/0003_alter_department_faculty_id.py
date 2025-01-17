# Generated by Django 4.1.3 on 2023-04-01 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_department_faculty_id_alter_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.faculty', verbose_name='دانشکده / دانشگاه'),
        ),
    ]
