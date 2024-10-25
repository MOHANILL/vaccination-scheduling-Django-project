from email.policy import default

from django.db import models

class Vaccine(models.Model):
    name = models.CharField("Vaccine_Name",max_length=32)
    description = models.TextField(max_length=1024)
    number_of_doses = models.IntegerField(default=1)
    interval = models.IntegerField(default=0, help_text="Please provide an interval in days")
    storage_temperature = models.IntegerField(null=True, blank=True, help_text="Provide temprature in Celcius")
    minimum_age = models.IntegerField(default=0)

    def __str__(self):
        return self.name