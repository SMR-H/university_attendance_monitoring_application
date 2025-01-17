# Generated by Django 4.1.3 on 2023-03-01 11:10

from django.db import migrations, models
import django.db.models.deletion
import validators.custom_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('degree_code', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('group_code', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('major_code', models.CharField(max_length=50, unique=True, validators=[validators.custom_validators.validate_only_digits])),
                ('degree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.degree')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.department')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.group')),
            ],
        ),
    ]
