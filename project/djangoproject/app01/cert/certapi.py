# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from app01.cert.models import Qiyeuser


@api_view(['POST', 'GET'])
def qyxxgl(request):
    username = request.POST.get('username')
    username = eval(username)
    obj = Qiyeuser.objects.filter(username=username).first()
    obj.logo = str(obj.logo)
    obj.mt = str(obj.mt)
    obj.video = str(obj.video)
    # print({obj.logo.name})
    qiyeinfo_data = {
        'qiyename': obj.qiyename,
        'qiyefaren': obj.qiyefaren,
        'logo': obj.logo,
        'mt': obj.mt,
        'video': obj.video,
    }
    # print(qiyeinfo_data)
    return Response(qiyeinfo_data)
    # return Response('ok')


@api_view(['POST', 'GET'])
def edit_qyxxgl(request):
    username = request.POST.get('username')
    username = eval(username)
    qiyename = request.POST['qiyename']
    qiyefaren = request.POST['qiyefaren']
    logo = request.POST.get('logo')
    mt = request.POST.get('mt')
    video = request.POST.get('video')
    if Qiyeuser.objects.filter(username=username).first() == None:
        Qiyeuser.objects.create(username=username)
    Qiyeuser.objects.filter(username=username).update(qiyename=qiyename, qiyefaren=qiyefaren, logo=logo, mt = mt, video=video)

    return Response('ok')


@api_view(['POST', 'GET'])
def edit_flzd(request):
    username = request.POST.get('username')
    # print(username)
    username = eval(username)
    # print(username)
    if Qiyeuser.objects.filter(username=username).first() == None:
            Qiyeuser.objects.create(username=username)
    obj = Qiyeuser.objects.filter(username=username).first()

    # print(username)
    qiyeinfo_data = {
        'qiyearea': obj.qiyearea,
        'WKHR': obj.WKHR,
        'ATO': obj.ATO,
        'overtime': obj.overtime,
        'fldy': obj.fldy,

    }
    # print(qiyeinfo_data)
    return Response(qiyeinfo_data)
    # return Response(username)

# 福利制度修改
@api_view(['POST', 'GET'])
def edit_addflzd(request):
    username = request.POST.get('username')
    # print(username)
    username = eval(username)
    print(username)
    qiyearea = request.POST.get('qiyearea')
    WKHR = request.POST.get('WKHR')
    ATO = request.POST.get('ATO')
    overtime = request.POST.get('overtime')
    fldy = request.POST.get('fldy')
    if Qiyeuser.objects.filter(username=username).first() == None:
        Qiyeuser.objects.create(username=username)
    Qiyeuser.objects.filter(username=username).update(qiyearea=qiyearea)
    Qiyeuser.objects.filter(username=username).update(WKHR=WKHR)
    Qiyeuser.objects.filter(username=username).update(ATO=ATO)
    Qiyeuser.objects.filter(username=username).update(overtime=overtime)
    Qiyeuser.objects.filter(username=username).update(fldy=fldy)

    data = {
        'qiyearea': qiyearea,
        'WKHR': WKHR,
        'ATO': ATO,
        'overtime': overtime,
        'fldy': fldy,
    }
    print(data)
    return Response('ok')


from rest_framework.viewsets import GenericViewSet
class BookInfoViewSet_logo(GenericViewSet):
    # 保存图片
    @action(methods=['post'], detail=False)
    def savelogo(self, request):
        file = request.FILES.get('file')
        try:
            # 构造图片保存路径
            file_path = './upload/' + file.name
            print(file_path)
            # 保存图片
            with open(file_path, 'wb+') as f:
                f.write(file.read())
                f.close()
            response = {'file': file.name, 'code': 200, 'msg': "添加成功"}
        except:
            response = {'file': '', 'code': 201, 'msg': "添加失败"}
        return Response(response)

class BookInfoViewSet_img(GenericViewSet):
    # 保存图片
    @action(methods=['post'], detail=False)
    def saveimg(self, request):
        file = request.FILES.get('file')
        try:
            # 构造图片保存路径
            file_path = './upload/qy_mt/' + file.name
            print(file_path)
            # 保存图片
            with open(file_path, 'wb+') as f:
                f.write(file.read())
                f.close()
            response = {'file': file.name, 'code': 200, 'msg': "添加成功"}
        except:
            response = {'file': '', 'code': 201, 'msg': "添加失败"}
        return Response(response)

class BookInfoViewSet_video(GenericViewSet):
    # 保存视频
    @action(methods=['post'], detail=False)
    def savevideo(self, request):
        file = request.FILES.get('file')
        try:
            # 构造图片保存路径
            file_path = './upload/qy_video/' + file.name
            print(file_path)
            # 保存图片
            with open(file_path, 'wb+') as f:
                f.write(file.read())
                f.close()
            response = {'file': file.name, 'code': 200, 'msg': "添加成功"}
        except:
            response = {'file': '', 'code': 201, 'msg': "添加失败"}
        return Response(response)

#企业介绍
@api_view(['POST', 'GET'])
def edit_qyjs(request):
    username = request.POST.get('username')
    # print(username)
    username = eval(username)
    # print(username)
    if Qiyeuser.objects.filter(username=username).first() == None:
            Qiyeuser.objects.create(username=username)
    obj = Qiyeuser.objects.filter(username=username).first()

    # print(username)
    qiyeinfo_data = {
        'jbjs': obj.jbjs,
        'cltime': obj.cltime,
        'http': obj.http,
        'zjob': obj.zjob,
        'fjob': obj.fjob,
        'type': obj.type,
        'qygm': obj.qygm,
        'rzzt': obj.rzzt,
    }
    # print(qiyeinfo_data)
    return Response(qiyeinfo_data)
    # return Response(username)

# 企业介绍修改
@api_view(['POST', 'GET'])
def edit_qyjssave(request):
    username = request.POST.get('username')
    # print(username)
    username = eval(username)
    print(username)
    jbjs = request.POST.get('jbjs')
    cltime = request.POST.get('cltime')
    http = request.POST.get('http')
    zjob = request.POST.get('zjob')
    fjob = request.POST.get('fjob')
    type = request.POST.get('type')
    qygm = request.POST.get('qygm')
    rzzt = request.POST.get('rzzt')
    if Qiyeuser.objects.filter(username=username).first() == None:
        Qiyeuser.objects.create(username=username)
    Qiyeuser.objects.filter(username=username).update(jbjs=jbjs)
    Qiyeuser.objects.filter(username=username).update(cltime=cltime)
    Qiyeuser.objects.filter(username=username).update(http=http)
    Qiyeuser.objects.filter(username=username).update(zjob=zjob)
    Qiyeuser.objects.filter(username=username).update(fjob=fjob)
    Qiyeuser.objects.filter(username=username).update(type=type)
    Qiyeuser.objects.filter(username=username).update(qygm=qygm)
    Qiyeuser.objects.filter(username=username).update(rzzt=rzzt)

    data = {
        'jbjs': jbjs,
        'cltime': cltime,
        'http': http,
        'zjob': zjob,
        'fjob': fjob,
        'type': type,
        'qygm': qygm,
        'rzzt': rzzt,
    }
    print(data)
    return Response('ok')
