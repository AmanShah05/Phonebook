from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    international_code = models.CharField(max_length=30)
    phone_number =  models.CharField(max_length=20)

    def __str__(self):
        return self.first_name