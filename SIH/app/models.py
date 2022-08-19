from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

GENDER_CHOICES = (
    ('M', "Male"),
    ("F", "Female"),
    ("O", "Other")
)


CATEGORY_CHOICES = (
    ('Gen', 'General'),
    ("OBC", "Other Backwards Caste"),
    ("SC", "Scheduled Caste"),
    ("ST", "Scheduled Tribe")
)


class Document(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')
    verified = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="profile_pic/", blank=True)

    # address
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.BigIntegerField()

    # personal Details
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    adhaar_number = models.BigIntegerField()
    phone_number = models.CharField(max_length=12)

    # educational details
    highest_qualification = models.CharField(max_length=50)

    # work details
    occupation = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    income = models.IntegerField()

    def __str__(self) -> str:
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    created_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class Scheme(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    img = models.ImageField(upload_to="scheme/")
    department = models.ForeignKey(Category, on_delete=models.CASCADE)

    #eligibility
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    category = models.CharField(max_length=50)
    income_min = models.IntegerField()
    income_max = models.IntegerField()
    gender = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return str(self.name)