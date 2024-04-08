from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token

import requests
import base64
import os
from app01.login.models import Userinfo


# 登录
@api_view(['POST', 'GET'])
def zhiku_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # address = request.POST.get('address')
    # real_name = request.POST.get('real_name')
    # age = request.POST.get('age')
    # job = request.POST.get('job')
    # 登录逻辑
    user = Userinfo.objects.filter(username=username).first()
    if user:
        # checkPwd = check_password(password, user[0].password)
        # print(checkPwd)
        # print(user[0].password)
        # print(password)
        # print(1)
        # if checkPwd:
        if password != user.password:
            # userinfo = Userinfo.objects.get_or_create(user = user).first()
            # userinfo = Userinfo.objects.get(user = user).first()
            # token = Token.objects.get_or_create(user=user).first()
            # token = Token.objects.get(user=user).first()
            return Response('pwderr')
        # else:
        #     return Response('pwderr')
    else:
        return Response('none')
    userinfo_data = {
        # 'token': token.key,
        'username': user.username,
        # 'address': user.address,
        # 'real_name':user.real_name,
        # 'age':user.age,
        # 'job':user.job,
    }
    # request.session["info"] = username
    return Response(userinfo_data)
    # user = 'zzz'
    # password = '123456'
    # data = {
    #     'user': user,
    #     'password': password
    # }
    # print(data)
    # return Response(data)


# 注册
@api_view(['POST'])
def zhiku_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    # 注册逻辑
    print(username, password)
    user = Userinfo.objects.filter(username=username).first()
    if user:
        return Response('repeat')
    else:
        new_password = make_password(password,username)
        # newUser = Userinfo(username=username , password=password)
        Userinfo.objects.create(username=username, password=password)
        print(username, password)
        # newUser.save()

    # token = Token.objects.get_or_create(user=newUser)
    # token = Token.objects.get(user=newUser)
    # userinfo = Userinfo.objects.get_or_create(belong=newUser)
    # userinfo = Userinfo.objects.get(belong=newUser)
    userinfo_data = {
        # 'token': token.key,
        'nickName': username,
    }
    return Response(userinfo_data)


# 个人信息
@api_view(['POST', 'GET'])
def geren(request):
    username = request.POST.get('username')
    username = eval(username)
    # print()
    obj = Userinfo.objects.filter(username=username).first()
    userinfo_data = {
        'address': obj.address,
        'real_name': obj.real_name,
        'job': obj.job,
        'age': obj.age,
        'grjj': obj.grjj,
        'password': obj.password,
        'checkPass': obj.password,
        'email': obj.email,
        'phone': obj.phone,
    }
    return Response(userinfo_data)


# 编辑个人信息
@api_view(['POST', 'GET'])
def edit_geren(request):
    username = request.POST.get('username')
    panduan = request.POST.get('panduan')
    print(panduan)
    username = eval(username)
    if panduan == "1":
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        Userinfo.objects.filter(username=username).update(email=email)
        Userinfo.objects.filter(username=username).update(phone=phone)
        Userinfo.objects.filter(username=username).update(password=password)
        data = {
            'email': email,
            'phone': phone,
            'password': password,
        }
        return Response(data)
    else:
        address = request.POST.get('address')
        real_name = request.POST.get('real_name')
        job = request.POST.get('job')
        age = request.POST.get('age')
        grjj = request.POST.get('grjj')

        Userinfo.objects.filter(username=username).update(address=address)
        Userinfo.objects.filter(username=username).update(real_name=real_name)
        Userinfo.objects.filter(username=username).update(job=job)
        Userinfo.objects.filter(username=username).update(age=age)
        Userinfo.objects.filter(username=username).update(grjj=grjj)

        data = {
            'address': address,
            'real_name': real_name,
            'job': job,
            'age': age,
            'grjj': grjj,
        }
        print(data)
        return Response(data)
    return Response('ok')

