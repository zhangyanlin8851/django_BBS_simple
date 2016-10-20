#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from dao import models

class Form1(forms.Form):
    username = forms.CharField(error_messages={'required': '用户名不能为空',})
    passwd = forms.CharField(error_messages={'required': '密码不能为空',})
    check = forms.CharField(error_messages={'required': '验证码不能为空',})

class Form2(forms.Form):
    title = forms.CharField(error_messages={'required': '标题不能为空',})
    content = forms.CharField(error_messages={'required': '内容不能为空',})
    img = forms.ImageField(error_messages={'required': '内容不能为空','invalid': '图片格式错误'})
    url = forms.CharField(error_messages={'required': '头像不能为空',})