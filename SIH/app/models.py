from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
# import json
# json_data = open()
# data1 = json.load(json_data) # deserialises it
# data2 = json.dumps(data1) # json formatted string

# json_data.close()


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

DOCUMENT_NAMES = (
    ('Aadhar', 'Aadhar'),
    ("Passport", "Passport"),
    ("Voter ID", "Voter ID"),
    ("Driving License", "Driving License"),
    ("Pan Card", "Pan Card"),
    ("Ration Card", "Ration Card"),
    ("Passport", "Passport"),
    ("Other", "Other")
)


class Document(models.Model):
    name = models.CharField(choices=DOCUMENT_NAMES, max_length=100)
    file = models.FileField(upload_to='documents/')
    verified = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="profile_pic/", blank=True)
    email_token = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)

    # address
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.BigIntegerField()

    # personal Details
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    adhaar_number = models.BigIntegerField(unique=True)
    phone_number = models.CharField(max_length=12)

    # educational details
    highest_qualification = models.CharField(max_length=50)

    # work details
    occupation = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    income = models.IntegerField()

    def __str__(self) -> str:
        return str(self.user)


class UserVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user)


DEPARTMENT_CHOICES = (
    ("IT", "IT"),
    ("Ag", "Agriculture"),
)


class Scheme(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()
    img = models.ImageField(upload_to="scheme/")
    department = models.CharField(max_length=50)

    # eligibility
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


class SchemeRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user) + " " + str(self.scheme)


class SchemeTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    benefitted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user) + " " + str(self.scheme)
