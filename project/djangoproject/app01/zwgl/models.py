from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Zhiwei(models.Model):
    username = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(null=True, blank=True, max_length=200)
    xingzhi = models.CharField(null=True, blank=True, max_length=200)
    describe = models.CharField(null=True, blank=True, max_length=200)
    leibie = models.CharField(null=True, blank=True, max_length=200)
    yaoqiu = models.CharField(null=True, blank=True, max_length=200)
    xueli = models.CharField(null=True, blank=True, max_length=200)
    key = models.CharField(null=True, blank=True, max_length=200)
    fuli = models.CharField(null=True, blank=True, max_length=200)
    address = models.CharField(null=True, blank=True, max_length=200)
    xinzi = models.CharField(null=True, blank=True, max_length=200)
    amount = models.CharField(null=True, blank=True, max_length=200)
    status = models.CharField(null=True, blank=True, max_length=200)
    # 1:待上线 2：已上线 3：审核中 4：未通过

    def __str__(self):
        return self.name
