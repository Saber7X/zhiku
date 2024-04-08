from django.contrib import admin
from app01.login.models import Userinfo
from app01.chat.models import zhaopin
from app01.cert.models import Qiyeuser
from app01.zwgl.models import Zhiwei
from app02.wenjuan.wjModels import Disc

# Register your models here.

admin.site.register(Userinfo)

admin.site.register(zhaopin)

admin.site.register(Qiyeuser)

admin.site.register(Zhiwei)
admin.site.register(Disc)
