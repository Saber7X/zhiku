from django.db import models
# Create your models here.


class Userinfo(models.Model):
    password = models.CharField(null=True, blank=True, max_length=200)
    username = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(null=True, blank=True, max_length=200)
    real_name = models.CharField(null=True, blank=True, max_length=200)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)
    grjj = models.CharField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=200)
    panduan = models.CharField(null=True, blank=True, max_length=200)