from django.db import models

class Holiday(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField(unique=True)

    def __str__(self):
        return f'{self.name} on {self.date}'