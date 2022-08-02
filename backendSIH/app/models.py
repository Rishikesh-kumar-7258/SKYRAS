from django.db import models


class User(models.Model):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.DateField()
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=50)
    createdDate = models.DateField()
    updatedDate = models.DateField()

    def __str__(self):
        return self.username


class Document(models.Model):
    documentID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    documentType = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    date = models.DateField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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