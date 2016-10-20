#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BaseResponse(object):

    def __init__(self):
        self.status = False
        self.message = ""
        self.data = ""