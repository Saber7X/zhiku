from django.db import models
from ..cert.models import Qiyeuser
# Create your models here.
class zhaopin(models.Model):
    gangwei = models.CharField(null=True, blank=True, max_length=200)
    area = models.CharField(null=True, blank=True, max_length=200)
    renshu = models.CharField(null=True, blank=True, max_length=200)
    xingzhi = models.CharField(null=True, blank=True, max_length=200)
    xinzi = models.CharField(null=True, blank=True, max_length=200)
    xueli = models.CharField(null=True, blank=True, max_length=200)
    describe = models.CharField(null=True, blank=True, max_length=200)
    call = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(null=True, blank=True, max_length=200)
    # belong_qiyeuser = models.ForeignKey(Qiyeuser, on_delete=models.CASCADE)
