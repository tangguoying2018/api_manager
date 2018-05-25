#!/usr/bin/env python
# coding: utf-8
# author: tang

from django import template
from django.contrib.auth.models import User
import hashlib
import time

register = template.Library()


@register.filter(name='gen_md5')
def gen_md5(api_id):
    new_md5 = hashlib.md5()
    new_md5.update(str(api_id))
    return new_md5.hexdigest()


@register.filter(name='get_username')
def get_username(uid):
    ret = User.objects.get(id=uid)
    return ret.username


@register.filter(name='get_time')
def get_time(timestamp):
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
    return dt


@register.filter(name='convert')
def convert(content):
    content = eval(content)
    return content
