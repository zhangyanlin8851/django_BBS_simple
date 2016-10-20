#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dao import models
import time
import os
import json
from commons import pager

def add_data(request):
    time_now = time.strftime("%Y-%m-%d %H:%M:%S")
    title = request.POST.get('title')
    content = request.POST.get('content')
    obj = request.FILES.get('img')

    username = request.session.get('username',None)
    user_id = models.Userinfo.objects.filter(username=username).values('id')
    user_id = int(list(user_id)[0]['id'])


    chunk_name = os.path.join('static', 'image', obj.name)
    f = open(chunk_name, 'wb')
    for chunk in obj.chunks():
        f.write(chunk)
    f.close()

    new_info = {
        'title':title,
        'content':content,
        'url':'/static/image/%s'%obj.name,
        'create_date':time_now,
        'user_id_id':user_id,
    }
    models.News.objects.create(**new_info)


def get_new(page):
    content_count = models.News.objects.count()
    obj = pager.Pagenation(page, content_count, '/index/')
    news = models.News.objects.all().order_by('-id')[obj.start:obj.end]
    # print(news)
    str_page = obj.string_pager()
    return news,str_page

def get_new_title(news_id):
    news_id = int(news_id)
    news = models.News.objects.filter(id = news_id).values('title','content','url','create_date','user_id__username').first()
    print(news)
    return news