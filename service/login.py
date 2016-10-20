#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dao import models
from  commons import Response



def logins(request,data):
    rep = Response.BaseResponse()
    obj = models.Userinfo.objects.filter(username=data['username'],passwd=data['passwd']).count()
    # print(request.session.get('check_code').upper(),data['check'].upper())
    if not obj:
        rep.data = "用户名密码错误"
        return rep
    if not request.session.get('check_code').upper() == data['check'].upper():
        rep.data = "验证码错误"
        return rep

    user_info_dict = {
        'username':data['username'],
        'passwd':data['passwd'],
    }
    request.session['is_login'] = True
    request.session.update(user_info_dict)
    rep.status = True
    return rep





