from django.db import models
import datetime

class Animal(models.Model):
    accept_num = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    build = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    accept_num = models.CharField(max_length=200)
    chip_num = models.CharField(max_length=200)
    is_sterilization = models.CharField(max_length=200)
    hair_type = models.CharField(max_length=200)
    note = models.TextField()
    resettlement = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    childre_anlong = models.CharField(max_length=200)
    animal_anlong = models.CharField(max_length=200)
    bodyweight = models.CharField(max_length=200)
    image_name = models.URLField(max_length=200)
    image_file = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

class User(models.Model):
    email = models.EmailField()
    is_fb = models.BooleanField()
    fb_access_token = models.CharField(max_length=200)
    fb_user_id = models.IntegerField()
    last_login_date = models.DateTimeField(auto_now=True)
