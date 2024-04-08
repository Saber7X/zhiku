from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import requests
import base64
import os
from app01.zwgl.models import Zhiwei
from app01.cert.models import Qiyeuser
from app02.login.models import Rencai, Userinfo1

@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def getHrm(request):
    key = request.POST.get('username')
    key = eval(key)
    data = Rencai.objects.filter(qiyeusername=key).values('qiyeusername', 'yonghuusername','status','zhiwei', 'id')
    data_list = [i for i in data]
    for i in data_list:
        i['name'] = Userinfo1.objects.filter(username=i['yonghuusername']).first().name
        i['age'] = Userinfo1.objects.filter(username=i['yonghuusername']).first().age
        i['gender'] = Userinfo1.objects.filter(username=i['yonghuusername']).first().gender
        i['address'] = Userinfo1.objects.filter(username=i['yonghuusername']).first().address
    # print(data_list)

    return Response(data_list)

# 收藏
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def HrmFav(request):
    id = request.POST.get('id')
    print("id",id)
    Rencai.objects.filter(id=id).update(status='1')
    return Response('ok')

# 不合适
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def HrmUnsa(request):
    id = request.POST.get('id')
    Rencai.objects.filter(id=id).update(status='2')
    return Response('ok')

# 删除
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def HrmDel(request):
    id = request.POST.get('id')
    Rencai.objects.filter(id=id).delete()
    return Response('ok')

# 详情
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def HrmDetail(request):
    id = request.POST.get('id')
    username = Rencai.objects.filter(id=id).first().yonghuusername
    data = Userinfo1.objects.filter(username=username).values().first()
    print(data)
    return Response(data)