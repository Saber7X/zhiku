from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from app02.login.models import Userinfo1
import requests
import base64
import os


# 登录
@api_view(['POST', 'GET'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 登录逻辑
    user = Userinfo1.objects.filter(username=username).first()
    if user:
        if password != user.password:
            return Response('pwderr')
    else:
        return Response('none')
    userinfo1_data = {
        'username': user.username,
    }
    # request.session["info"] = username
    return Response(userinfo1_data)


# 注册
@api_view(['POST'])
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    phone = request.POST.get('phone')
    # 注册逻辑
    print(username, password)
    user = Userinfo1.objects.filter(username=username).first()
    if user:
        return Response('repeat')
    else:
        if len(username) > 20:
            return ('nameerr')
        if password != password2:
            return ('pwderr')
        if len(password) > 16:
            return ('pwderr1')
        if len(phone) != 11:
            return ('phoneerr')
        Userinfo1.objects.create(username=username, password=password, phone=phone)
        print(username, password)
    userinfo1_data = {
        # 'token': token.key,
        'nickName': username,
    }
    return Response(userinfo1_data)


 # 用户个人信息
@api_view(['POST', 'GET'])
def grxx(request):
    username = request.POST.get('username')
    username = eval(username)
    print(username)
    obj = Userinfo1.objects.filter(username=username).first()
    userinfo1_data = {
        'name': obj.name,
        'gender': obj.gender,
        'age': obj.age,
        'address': obj.address,
        'identity': obj.identity,
        'phone': obj.phone,
        'email': obj.email,
    }
    # return Response('ok')
    return Response(userinfo1_data)

# 编辑个人信息
@api_view(['POST', 'GET'])
def grxxsave(request):
    username = request.POST.get('username')
    #panduan = request.POST.get('panduan')
    username = eval(username)
    print(username)
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    address = request.POST.get('address')
    identity = request.POST.get('identity')
    phone = request.POST.get('phone')
    email = request.POST.get('email')

    Userinfo1.objects.filter(username=username).update(name=name)
    Userinfo1.objects.filter(username=username).update(gender=gender)
    Userinfo1.objects.filter(username=username).update(age=age)
    Userinfo1.objects.filter(username=username).update(address=address)
    Userinfo1.objects.filter(username=username).update(identity=identity)
    Userinfo1.objects.filter(username=username).update(phone=phone)
    Userinfo1.objects.filter(username=username).update(email=email)

    data = {
        'name': name,
        'gender': gender,
        'age': age,
        'address': address,
        'identity': identity,
        'phone': phone,
        'email': email,
    }
    return Response(data)

 # 用户个人优势
@api_view(['POST', 'GET'])
def grys(request):
    username = request.POST.get('username')
    username = eval(username)
    print(username)
    obj = Userinfo1.objects.filter(username=username).first()
    userinfo1_data = {
        'advantage': obj.advantage,
    }
    # return Response('ok')
    return Response(userinfo1_data)

# 编辑个人优势
@api_view(['POST', 'GET'])
def gryssave(request):
    username = request.POST.get('username')
    #panduan = request.POST.get('panduan')
    username = eval(username)
    print(username)
    advantage = request.POST.get('advantage')
    Userinfo1.objects.filter(username=username).update(advantage=advantage)
    data = {
        'advantage': advantage,
    }
    return Response(data)

 # 用户期望职位
@api_view(['POST', 'GET'])
def qwzw(request):
    username = request.POST.get('username')
    username = eval(username)
    print(username)
    obj = Userinfo1.objects.filter(username=username).first()
    userinfo1_data = {
        'work': obj.work,
        'qwyx': obj.qwyx,
    }
    # return Response('ok')
    return Response(userinfo1_data)

# 编辑期望职位
@api_view(['POST', 'GET'])
def qwzwsave(request):
    username = request.POST.get('username')
    #panduan = request.POST.get('panduan')
    username = eval(username)
    print(username)
    work = request.POST.get('work')
    qwyx = request.POST.get('qwyx')
    Userinfo1.objects.filter(username=username).update(work=work)
    Userinfo1.objects.filter(username=username).update(qwyx=qwyx)
    data = {
        'work': work,
        'qwyx': qwyx,
    }
    return Response(data)

 # 用户工作经历
@api_view(['POST', 'GET'])
def gzjl(request):
    username = request.POST.get('username')
    username = eval(username)
    print(username)
    obj = Userinfo1.objects.filter(username=username).first()
    userinfo1_data = {
        'gsmc': obj.gsmc,
        'timeq': obj.timeq,
        'timez': obj.timez,
        'job': obj.job,
    }
    # return Response('ok')
    return Response(userinfo1_data)

# 编辑用户工作经历
@api_view(['POST', 'GET'])
def gzjlsave(request):
    username = request.POST.get('username')
    #panduan = request.POST.get('panduan')
    username = eval(username)
    print(username)
    gsmc = request.POST.get('gsmc')
    timeq = request.POST.get('timeq')
    timez = request.POST.get('timez')
    job = request.POST.get('job')
    Userinfo1.objects.filter(username=username).update(gsmc=gsmc)
    Userinfo1.objects.filter(username=username).update(timeq=timeq)
    Userinfo1.objects.filter(username=username).update(timez=timez)
    Userinfo1.objects.filter(username=username).update(job=job)
    data = {
        'gsmc': gsmc,
        'timeq': timeq,
        'timez': timez,
        'job': job,
    }
    return Response(data)

 # 用户教育经历
@api_view(['POST', 'GET'])
def jyjl(request):
    username = request.POST.get('username')
    username = eval(username)
    print(username)
    obj = Userinfo1.objects.filter(username=username).first()
    userinfo1_data = {
        'school': obj.school,
        'degree': obj.degree,
        'profession': obj.profession,
        'etimeq': obj.etimeq,
        'etimez': obj.etimez,
    }
    # return Response('ok')
    return Response(userinfo1_data)

# 编辑教育经历
@api_view(['POST', 'GET'])
def jyjlsave(request):
    username = request.POST.get('username')
    #panduan = request.POST.get('panduan')
    username = eval(username)
    print(username)
    school = request.POST.get('school')
    degree = request.POST.get('degree')
    profession = request.POST.get('profession')
    etimeq = request.POST.get('etimeq')
    etimez = request.POST.get('etimez')
    Userinfo1.objects.filter(username=username).update(school=school)
    Userinfo1.objects.filter(username=username).update(degree=degree)
    Userinfo1.objects.filter(username=username).update(profession=profession)
    Userinfo1.objects.filter(username=username).update(etimeq=etimeq)
    Userinfo1.objects.filter(username=username).update(etimez=etimez)
    data = {
        'school': school,
        'degree': degree,
        'profession': profession,
        'etimeq': etimeq,
        'etimez': etimez,
    }
    return Response(data)
# 用户技能荣誉
@api_view(['POST', 'GET'])
def jnry(request):
    username = request.POST.get('username')
    username = eval(username)
    print(username)
    obj = Userinfo1.objects.filter(username=username).first()
    userinfo1_data = {
        'success': obj.success,
    }
    # return Response('ok')
    return Response(userinfo1_data)

# 编辑技能荣誉
@api_view(['POST', 'GET'])
def jnrysave(request):
    username = request.POST.get('username')
    #panduan = request.POST.get('panduan')
    username = eval(username)
    print(username)
    success = request.POST.get('success')
    Userinfo1.objects.filter(username=username).update(success=success)
    data = {
        'success': success,
    }
    return Response(data)