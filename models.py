from django.db import models

# Create your models here.
class ContactData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    course=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
