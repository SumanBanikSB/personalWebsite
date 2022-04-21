from django.db import models
from students.models import Student
from django.urls import reverse


# Create your models here.
class Homework(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    topic = models.CharField(max_length = 50)
    images = models.ImageField(default = False,upload_to = 'hwImages')

    class Meta:
        ordering = ['student','topic','images']


    def __str__(self):
        return f"{self.student} has been assigned {self.topic}"

    def get_absolute_url(self):
        return reverse("homework_detail", kwargs={"pk": self.pk})
    