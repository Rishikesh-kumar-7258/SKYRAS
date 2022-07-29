from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middleName = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)


class Document(models.Model):
    documentID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    documentType = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    file = models.FileField()
    date = models.DateField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Scheme(models.Model):
    schemeID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    startdate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
