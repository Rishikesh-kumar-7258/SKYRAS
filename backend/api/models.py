from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_OPTIONS  = (
    ("1" , "MALE"),
    ("2" , "FEMALE"),
    ("3" , "OTHER")
)

CATERGORY_OPTIONS = (
    ("1" , "GENERAL"),
    ("2" , "OBC"),
    ("3" , "SC"),
    ("4" , "ST"),
    ("5" , "EWS")
)

class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pin_code = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    aadhar_number = models.BigIntegerField(blank=False, null=False)
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=20)
    dob = models.DateField()
    category = models.CharField(choices=CATERGORY_OPTIONS, max_length=20)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name + self.middle_name + self.last_name


class Statistics(models.Model):

    registered_users = models.IntegerField()
    total_amount_paid = models.BigIntegerField()
    total_users_benefited = models.IntegerField()

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'

    def __str__(self):
        return self.name


class Scheme(models.Model):
    name = models.CharField(max_length=50, blank=False)
    desc = models.CharField(max_length=500)
    eligible_genders = models.CharField(choices=GENDER_OPTIONS, max_length=20)
    eligible_category = models.CharField(choices=CATERGORY_OPTIONS, max_length=20)
    min_annual_income = models.BigIntegerField()
    max_annual_income = models.BigIntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    min_family_members = models.IntegerField()
    max_family_members = models.IntegerField()
    eligible_states = models.CharField(max_length=20)
    eligible_districts = models.CharField(max_length=20)
    eligible_cities = models.CharField(max_length=20)
    eligible_pincodes = models.CharField(max_length=20)
    stats = models.ForeignKey(Statistics, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Scheme'
        verbose_name_plural = 'Schemes'

    def __str__(self):
        return self.name