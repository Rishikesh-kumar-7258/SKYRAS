from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_OPTIONS  = {
    "1" : "MALE",
    "2" : "FEMALE",
    "3" : "OTHER"
}

CATERGORY_OPTIONS = {
    "1" : "GENERAL",
    "2" : "OBC",
    "3" : "SC",
    "4" : "ST",
    "5" : "EWS"
}

class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pin_code = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    aadhar_number = models.BigIntegerField(blank=False, null=False)
    gender = models.CharField(options=GENDER_OPTIONS)
    dob = models.DateField()
    category = models.CharField(options=CATERGORY_OPTIONS)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + self.middle_name + self.last_name