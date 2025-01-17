from django.db import models

# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=250, verbose_name='استان')
    province_code = models.PositiveSmallIntegerField(unique=True, db_index=True, verbose_name='کد استان')
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250, verbose_name='شهر')
    city_code = models.PositiveSmallIntegerField(unique=True, db_index=True, verbose_name='کد شهر')
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='استان')
    def __str__(self):
        return self.name