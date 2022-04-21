from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    GENDER_CHOISES = [('Male','male'),('Female','female')]
    status = [('Active','active'),('Inactive','inactive')]
    current_status = models.CharField(max_length=10,choices=status)
    registration_number = models.CharField(max_length=15,unique=False) # have to be unique = True.
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    gender = models.CharField(max_length =10,choices = GENDER_CHOISES,default = "Male")
    date_of_birth = models.DateField(default= timezone.now)
    email = models.EmailField()

    class Meta:
        ordering = ['last_name','first_name','registration_number']

    def __str__(self):
        return f"{self.last_name} {self.first_name} having a reg no. {self.registration_number}"

    # For the URL 
    def get_absolute_url(self):
        return reverse("student-details", kwargs={"pk": self.pk})
    
