# Generated by Django 4.1.3 on 2023-04-01 10:28

from django.db import migrations, models
import django.db.models.deletion
import validators.custom_validators


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='degree_id',
        ),
        migrations.RemoveField(
            model_name='major',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='major',
            name='major_code',
        ),
        migrations.RemoveField(
            model_name='major',
            name='name',
        ),
        migrations.CreateModel(
            name='MajorList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('major_code', models.CharField(max_length=50, unique=True, validators=[validators.custom_validators.validate_only_digits])),
                ('degree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.degree')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.group')),
            ],
        ),
        migrations.AddField(
            model_name='major',
            name='major_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='major.majorlist'),
            preserve_default=False,
        ),
    ]
