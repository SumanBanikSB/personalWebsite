from django.db import models

# Create your models here.
class Info(models.Model):
    first_name = models.CharField(max_length=20)
    dob = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} and {self.dob}'
