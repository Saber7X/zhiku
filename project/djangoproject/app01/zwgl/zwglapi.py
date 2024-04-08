from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import requests
import base64
import os

from app01.cert.models import Qiyeuser
from app01.zwgl.models import Zhiwei


# 职位发布
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4', 'GET'])
def Zhiweifabu(request):
    st = request.POST.get('st')
    if st == "GET1":
        username1 = request.POST.get('username')
        username1 = username1[1:-1]
        # print(username1)
        data=Zhiwei.objects.filter(username=username1, status='1').values("name")
        return Response(data)

    if st == "GET2":
        username1 = request.POST.get('username')
        username1 = username1[1:-1]
        # print(username1)
        data=Zhiwei.objects.filter(username=username1, status='2').values("name")
        return Response(data)

    if st == "GET3":
        username1 = request.POST.get('username')
        username1 = username1[1:-1]
        # print(username1)
        data=Zhiwei.objects.filter(username=username1, status='3').values("name")
        return Response(data)

    if st == "GET4":
        username1 = request.POST.get('username')
        username1 = username1[1:-1]
        # print(username1)
        data=Zhiwei.objects.filter(username=username1, status='4').values("name")
        return Response(data)

    data1 = {
        'username': request.POST.get('username'),
        'name': request.POST.get('name'),
        'xingzhi': request.POST.get('xingzhi'),
        'describe': request.POST.get('describe'),
        'leibie': request.POST.get('leibie'),
        'yaoqiu': request.POST.get('yaoqiu'),
        'xueli': request.POST.get('xueli'),
        'key': request.POST.get('key'),
        'fuli': request.POST.get('fuli'),
        'address': request.POST.get('address'),
        'xinzi': request.POST.get('xinzi'),
        'amount': request.POST.get('amount'),
        'status': request.POST.get('status'),
    }

    str = data1['username']
    str = str[1:-1]
    data1['username'] = str
    print(data1)
    Zhiwei.objects.create(**data1)
    return Response('ok')


# 职位上线
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def Zhiweionline(request):
    username1 = request.POST.get('username')
    username1 = username1[1:-1]
    name1 = request.POST.get('st')
    print(username1, name1)
    Zhiwei.objects.filter(username=username1, name=name1).update(status="3")
    return Response('ok')


# 职位下线
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def Zhiweidisonline(request):
    username1 = request.POST.get('username')
    username1 = username1[1:-1]
    name1 = request.POST.get('st')
    print(username1, name1)
    Zhiwei.objects.filter(username=username1, name=name1).update(status="1")
    return Response('ok')



# 职位修改
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def Zhiweiedit(request):
    stt = request.POST.get('stt')

    if stt == "123":
        username1 = request.POST.get('username')
        print(username1)
        username1 = username1[1:-1]
        name1 = request.POST.get('st')
        data1 = {
            'username': Zhiwei.objects.filter(username=username1, name=name1).first().username,
            'name': Zhiwei.objects.filter(username=username1, name=name1).first().name,
            'xingzhi': Zhiwei.objects.filter(username=username1, name=name1).first().xingzhi,
            'describe': Zhiwei.objects.filter(username=username1, name=name1).first().describe,
            'leibie': Zhiwei.objects.filter(username=username1, name=name1).first().leibie,
            'yaoqiu': Zhiwei.objects.filter(username=username1, name=name1).first().yaoqiu,
            'xueli': Zhiwei.objects.filter(username=username1, name=name1).first().xueli,
            'key':  Zhiwei.objects.filter(username=username1, name=name1).first().key,
            'fuli': Zhiwei.objects.filter(username=username1, name=name1).first().fuli,
            'address': Zhiwei.objects.filter(username=username1, name=name1).first().address,
            'xinzi': Zhiwei.objects.filter(username=username1, name=name1).first().xinzi,
            'amount': Zhiwei.objects.filter(username=username1, name=name1).first().amount,
            'status': Zhiwei.objects.filter(username=username1, name=name1).first().status,
        }
        return Response(data1)

    username1 = request.POST.get('username')
    name1 = request.POST.get('yuan_name')
    print(username1, name1)
    data1 = {
        'username': request.POST.get('username'),
        'name': request.POST.get('name'),
        'xingzhi': request.POST.get('xingzhi'),
        'describe': request.POST.get('describe'),
        'leibie': request.POST.get('leibie'),
        'yaoqiu': request.POST.get('yaoqiu'),
        'xueli': request.POST.get('xueli'),
        'key': request.POST.get('key'),
        'fuli': request.POST.get('fuli'),
        'address': request.POST.get('address'),
        'xinzi': request.POST.get('xinzi'),
        'amount': request.POST.get('amount'),
        'status': request.POST.get('status'),
    }
    Zhiwei.objects.filter(username=username1, name=name1).update(**data1)
    return Response('ok')


# 职位删除
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def Zhiweidelete(request):
    username1 = request.POST.get('username')
    print(username1)
    username1 = username1[1:-1]
    name1 = request.POST.get('st')
    Zhiwei.objects.filter(username=username1, name=name1).delete()
    return Response('ok')

@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def getZhiweiget(request):

    data = Zhiwei.objects.values( 'username','name', 'address', 'xinzi', 'xueli').values()
    data_list = [i for i in data]
    print(data_list)
    # 'qiyearea': obj.qiyearea,
    # 'WKHR': obj.WKHR,
    # 'ATO': obj.ATO,
    # 'overtime': obj.overtime,
    # 'fldy': obj.fldy,
    for i in data_list:
        i['qiyename']= Qiyeuser.objects.filter(username=i['username']).first().qiyename
        i['WKHR']= Qiyeuser.objects.filter(username=i['username']).first().WKHR
        i['ATO']= Qiyeuser.objects.filter(username=i['username']).first().ATO
        i['overtime']= Qiyeuser.objects.filter(username=i['username']).first().overtime
        i['fldy']= Qiyeuser.objects.filter(username=i['username']).first().fldy
        i['type'] = Qiyeuser.objects.filter(username=i['username']).first().type
        i['rzzt'] = Qiyeuser.objects.filter(username=i['username']).first().rzzt
        i['qygm'] = Qiyeuser.objects.filter(username=i['username']).first().qygm
        print(i)
    # print(data)
    return Response(data_list)

@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def ZhiweiDetail(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    data = Zhiwei.objects.filter(name=name, username=username).values('username', 'name', 'address', 'xinzi', 'xueli', 'xingzhi', 'describe', 'yaoqiu',)
    data_list = [i for i in data]
    for i in data_list:
        i['qiyename']= Qiyeuser.objects.filter(username=i['username']).first().qiyename
        i['WKHR']= Qiyeuser.objects.filter(username=i['username']).first().WKHR
        i['ATO']= Qiyeuser.objects.filter(username=i['username']).first().ATO
        i['overtime']= Qiyeuser.objects.filter(username=i['username']).first().overtime
        i['fldy']= Qiyeuser.objects.filter(username=i['username']).first().fldy
        i['logo']=Qiyeuser.objects.filter(username=i['username']).first().logo
        i['qiyearea']=Qiyeuser.objects.filter(username=i['username']).first().qiyearea

    print(data_list)

    return Response(data_list)


from app02.login.models import Rencai
@api_view(['POST', 'GET1', 'GET2', 'GET3', 'GET4','GET'])
def submitJianli(request):
    yonghuusername = request.POST.get('yonghuusername')
    yonghuusername = eval(yonghuusername)
    qiyeusername = request.POST.get('gongsiusername')
    zhiwei = request.POST.get('zhiwei')
    print(zhiwei)
    if Rencai.objects.filter(qiyeusername=qiyeusername, yonghuusername=yonghuusername, zhiwei=zhiwei).first() != None:
        return Response('repeat')
    Rencai.objects.create(qiyeusername=qiyeusername, yonghuusername=yonghuusername, zhiwei=zhiwei, )
    return Response('ok')