from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    blood_group = models.CharField(max_length=50)
    identity_document_type = models.CharField(max_length=50)
    identity_document_number = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_joined = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name +" | "+ self.last_name +" | "+self.date_of_birth