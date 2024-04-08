from djangoproject.urls import path
from app01.login import api
from app01.cert import certapi
from app01.zwgl import zwglapi
from app01.cert.certapi import BookInfoViewSet_logo, BookInfoViewSet_img, BookInfoViewSet_video
from app01.hrm.hrmapi import getHrm, HrmUnsa, HrmFav, HrmDel, HrmDetail

urlpatterns = [
    # 登录
    path('zhiku-login/', api.zhiku_login),
    # 注册
    path('zhiku-register/', api.zhiku_register),
    # 登出
    # path('zhiku-logout/', api.zhiku_logout),

    # 个人信息
    path('zhiku-geren/', api.geren),
    # 编辑个人信息
    path('edit/zhiku-geren/', api.edit_geren),
    # 企业信息

    path('zhiku-qyxxgl/', certapi.qyxxgl),
    # 编辑企业信息
    path('edit/zhiku-qyxxgl/', certapi.edit_qyxxgl),

    # 保存logo
    path('savelogo/', BookInfoViewSet_logo.as_view({'post': 'savelogo'})),
    # 保存美图
    path('saveimg/', BookInfoViewSet_img.as_view({'post': 'saveimg'})),
    # 保存视频
    path('savevideo/', BookInfoViewSet_video.as_view({'post': 'savevideo'})),

    #福利制度
    path('edit/zhiku-flzd/', certapi.edit_flzd),
    #编辑福利制度
    path('edit/zhiku-addflzd/', certapi.edit_addflzd),

    #  发布职位
    path('zhiweifabu/', zwglapi.Zhiweifabu),
    #  职位上线
    path('zhiweionline/', zwglapi.Zhiweionline),
    #  职位下线
    path('zhiweidisonline/', zwglapi.Zhiweidisonline),
    #  职位下线
    path('zhiweiedit/', zwglapi.Zhiweiedit),
    #  职位删除
    path('zhiweidelete/', zwglapi.Zhiweidelete),

    # 获取职位
    path('getzhiwei/', zwglapi.getZhiweiget),
    # 职位详情
    path('zhiwei-detail/', zwglapi.ZhiweiDetail),

    # 企业介绍
    path('edit/zhiku-qyjs/', certapi.edit_qyjs),
    # 编辑企业介绍
    path('edit/zhiku-qyjssave/', certapi.edit_qyjssave),

    # 获取职位
    path('getzhiwei/', zwglapi.getZhiweiget),
    # 职位详情
    path('zhiwei-detail/', zwglapi.ZhiweiDetail),

    # 获取人才
    path('gethrm/', getHrm),
    # 人才不合适
    path('hrm-unsa/', HrmUnsa),
    # 收藏人才
    path('hrm-fav/', HrmFav),
    # 删除人才
    path('hrm-del/', HrmDel),
    # 删除详情
    path('hrm-detail/', HrmDetail),

]