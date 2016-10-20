#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
import io
from commons import check_code
from service.form import *
from service.login import logins
from service.manager import add_data
from service.manager import get_new
from service.manager import get_new_title


def index(request,page):
    if request.method == "POST":
        rep = get_new_title(request)
        return HttpResponse(rep)
    if request.method == "GET":
        session = request.session
        news,str_page = get_new(page)
        return render(request,'index.html',{'session':session,'news':news,"page":str_page})

def login(request):
    if request.method == 'POST':
        # 获取请求内容做验证
        f = Form1(request.POST)
        if f.is_valid():
            ret = logins(request,f.cleaned_data)
            if ret.status:
                return redirect('/index/')
            else:
                return render(request, 'login.html', {'ret': ret,})
        else:
            return render(request,'login.html',{'error':f.errors,'form':f})
    else:
        return render(request,'login.html')

def check(request):
    steram = io.BytesIO()
    img, code = check_code.create_validate_code()
    img.save(steram, "png")
    request.session['check_code'] = code
    return HttpResponse(steram.getvalue())


def manager(request):
    if request.method == 'POST':
        # 获取请求内容做验证
        add_data(request)
        return redirect('/index/')
    else:
        return render(request,'manager.html')


def news_content(request,news_id):
    news = get_new_title(news_id)
    return render(request,'content.html',{'new':news})