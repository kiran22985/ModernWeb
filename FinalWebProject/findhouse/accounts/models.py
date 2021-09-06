from django.db import models
from django.core import validators
from django.core.validators import *
from django.contrib.auth.models import User

class Register(models.Model):
    Fullname=models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(4)])
    Email = models.EmailField(unique=True, null=True, validators=[validate_email])
    Phone = models.CharField(max_length=200, validators=[validators.MinLengthValidator(10)])
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Confirm_password=models.CharField(max_length=200)

class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username=models.CharField(max_length=200, null=True)
    firstname=models.CharField(max_length=200, null=True)
    lastname=models.CharField(max_length=200, null=True)
    email=models.EmailField(unique=True, null=True)
    phone=models.CharField(max_length=200, null=True)
    profile_pic=models.FileField(upload_to='static/uploads',default='static/image/bedroom.jpg')
    created_date=models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.username