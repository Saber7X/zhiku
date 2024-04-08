from django.db import models
# from ..login.models import Userinfo

# Create your models here.

class Qiyeuser(models.Model):
    username = models.CharField(null=True, blank=True, max_length=200)
    headimg = models.ImageField(upload_to='', null=True, blank=True)
    zhiwu = models.CharField(null=True, blank=True, max_length=200)
    shengfenzh = models.CharField(null=True, blank=True, max_length=200)
    qiyename = models.CharField(null=True, blank=True, max_length=200)
    qiyefaren = models.CharField(null=True, blank=True, max_length=200)
    qiyearea = models.CharField(null=True, blank=True, max_length=200)
    logo = models.CharField(null=True, blank=True, max_length=200)
    qiyetupian = models.ImageField(null=True, blank=True)
    WKHR = models.CharField(null=True, blank=True, max_length=200)
    ATO = models.CharField(null=True, blank=True, max_length=200)
    overtime = models.CharField(null=True, blank=True, max_length=200)
    fldy = models.CharField(null=True, blank=True, max_length=200)
    mt = models.CharField(null=True, blank=True, max_length=200)
    video = models.CharField(null=True, blank=True, max_length=200)
    jbjs = models.CharField(null=True, blank=True, max_length=200)
    cltime = models.CharField(null=True, blank=True, max_length=200)
    http = models.CharField(null=True, blank=True, max_length=200)
    zjob = models.CharField(null=True, blank=True, max_length=200)
    fjob = models.CharField(null=True, blank=True, max_length=200)
    type = models.CharField(null=True, blank=True, max_length=200)
    qygm = models.CharField(null=True, blank=True, max_length=200)
    rzzt = models.CharField(null=True, blank=True, max_length=200)
    # belong_qiye = models.CharField(null=True, blank=True, max_length=200)
    # belong_User = models.ForeignKey(Userinfo, on_delete=models.CASCADE)

# class Qiye(models.Model):
#     qiyeid = models.CharField(null=True, blank=True, max_length=200)
#     qiyename = models.CharField(null=True, blank=True, max_length=200)
#     qiyefaren = models.CharField(null=True, blank=True, max_length=200)
#     qiyearea = models.CharField(null=True, blank=True, max_length=200)
#     qiyeleixing = models.CharField(null=True, blank=True, max_length=200)
#     zuzhijigou = models.CharField(null=True, blank=True, max_length=200)
#     yingyezhizhao = models.CharField(null=True, blank=True, max_length=200)
#     belong_qiyeuser = models.ForeignKey(Qiyeuser, on_delete=models.CASCADE)
#
# class Qiyejianli(models.Model):
#     belong_user = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
#     belong_qiye = models.ForeignKey(Qiye, on_delete=models.CASCADE)
#
# class Qiyejibenxinxi(models.Model):
#     logo = models.ImageField(null=True, blank=True)
#     qiyetupian = models.ImageField(null=True, blank=True)
#     xingzhi = models.CharField(null=True, blank=True, max_length=200)
#     guimo = models.CharField(null=True, blank=True, max_length=200)
#     status = models.CharField(null=True, blank=True, max_length=200)
#     guanwang = models.CharField(null=True, blank=True, max_length=200)
#     address = models.CharField(null=True, blank=True, max_length=200)
#     worktime = models.CharField(null=True, blank=True, max_length=200)
#     belong_qiye = models.ForeignKey(Qiye, on_delete=models.CASCADE)



