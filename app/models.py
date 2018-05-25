# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Cate(models.Model):
    aid = models.AutoField(primary_key=True, verbose_name=u"分类id")
    cname = models.CharField(max_length=200, verbose_name=u'分类名称')
    cdesc = models.CharField(max_length=200, verbose_name=u'分类描述')
    isdel = models.IntegerField(default=0, verbose_name=u'是否删除{0:正常,1删除}')
    addtime = models.IntegerField(default=0, verbose_name=u'添加时间')

    class Meta:
        verbose_name = "接口分类表"
        db_table = "cate"


class Api(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u"接口编号")
    aid = models.IntegerField(default=0, verbose_name=u'接口分类id')
    num = models.CharField(max_length=100, null=True, verbose_name=u'接口编号')
    url = models.CharField(max_length=240, null=True, verbose_name=u'请求地址')
    name = models.CharField(max_length=100, null=True, verbose_name=u'接口名')
    des = models.CharField(max_length=300, null=True, verbose_name=u'接口描述')
    parameter = models.TextField(verbose_name=u'请求参数{所有的主求参数,以json格式在此存放}')
    memo = models.TextField(verbose_name=u'备注')
    re = models.TextField(verbose_name=u'返回值')
    lasttime = models.IntegerField(null=True, verbose_name=u'提后操作时间')
    firstuid = models.IntegerField(null=True, verbose_name=u'首次增加uid')
    lastuid = models.IntegerField(null=True, verbose_name=u'最后修改uid')
    isdel = models.IntegerField(default=0, verbose_name=u'{0:正常,1:删除}')
    type = models.CharField(null=True, max_length=11, verbose_name=u'请求方式')
    ord = models.IntegerField(default=0, verbose_name=u'排序(值越大,越靠前)')

    class Meta:
        verbose_name = "接口明细表"
        db_table = "api"
