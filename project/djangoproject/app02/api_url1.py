"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app02.login import api
from app01.zwgl.zwglapi import submitJianli
from app02.wenjuan.wjApi import Discget,DiscTest

urlpatterns = [
    path('yonghu-login/', api.login),
    path('yonghu-register/', api.register),
    # 用户个人信息
    path('grxx/', api.grxx),
    path('grxxsave/', api.grxxsave),
    # 用户个人优势
    path('grys/', api.grys),
    path('gryssave/', api.gryssave),
    # 用户期望职位
    path('qwzw/', api.qwzw),
    path('qwzwsave/', api.qwzwsave),
    # 用户工作经历
    path('gzjl/', api.gzjl),
    path('gzjlsave/', api.gzjlsave),
    # 用户教育经历
    path('jyjl/', api.jyjl),
    path('jyjlsave/', api.jyjlsave),
    # 用户技能荣誉
    path('jnry/', api.jnry),
    path('jnrysave/', api.jnrysave),

    # 提交简历
    path('submit-jianli/', submitJianli),

    #disc问卷
    path('disc/', Discget),
    path('disctest/', DiscTest),

]
