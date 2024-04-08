from django.db import models


# Create your models here.
class Userinfo1(models.Model):
    username = models.CharField(null=True, blank=True, max_length=200)
    password = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(null=True, blank=True, max_length=200)
    gender = models.CharField(null=True, blank=True, max_length=200)
    age = models.CharField(null=True, blank=True, max_length=200)
    address = models.CharField(null=True, blank=True, max_length=200)
    identity = models.CharField(null=True, blank=True, max_length=200)
    phone = models.CharField(null=True, blank=True, max_length=200)
    email = models.CharField(null=True, blank=True, max_length=200)
    advantage = models.CharField(null=True, blank=True, max_length=200)
    work = models.CharField(null=True, blank=True, max_length=200)
    qwyx = models.CharField(null=True, blank=True, max_length=200)
    gsmc = models.CharField(null=True, blank=True, max_length=200)
    timeq = models.CharField(null=True, blank=True, max_length=200)
    timez = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)
    school = models.CharField(null=True, blank=True, max_length=200)
    degree = models.CharField(null=True, blank=True, max_length=200)
    profession = models.CharField(null=True, blank=True, max_length=200)
    etimeq = models.CharField(null=True, blank=True, max_length=200)
    etimez = models.CharField(null=True, blank=True, max_length=200)
    success = models.CharField(null=True, blank=True, max_length=200)
    # status = models.CharField(null=True, blank=True, max_length=200, default="0")  # 0未查看  1收藏  2不合适
    # qiyeusername = models.CharField(null=True, blank=True, max_length=200)
    # yonghuusername = models.CharField(null=True, blank=True, max_length=200)
    # zhiwei = models.CharField(null=True, blank=True, max_length=200)


class Rencai(models.Model):
    qiyeusername = models.CharField(null=True, blank=True, max_length=200)
    yonghuusername = models.CharField(null=True, blank=True, max_length=200)
    zhiwei = models.CharField(null=True, blank=True, max_length=200)
    # Ren
    status = models.CharField(null=True, blank=True, max_length=200, default="0") # 0未查看  1收藏  2不合适

