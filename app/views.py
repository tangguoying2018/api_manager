# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cate, Api
import time
from django.http import HttpResponseRedirect


def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')


def index(request):
    all_cate = Cate.objects.all()
    return render(request, 'index.html', locals())


@login_required
def new_class(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cdesc = request.POST['cdesc']
        addtime = int(time.time())
        Cate.objects.create(cname=cname, cdesc=cdesc, addtime=addtime)
    return HttpResponseRedirect('/')


@login_required
def edit_class(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cdesc = request.POST['cdesc']
        aid = request.POST['aid']
        print "edit_class - aid: {}".format(aid)
        try:
            get_class = Cate.objects.get(aid=int(aid))
            get_class.cname = cname
            get_class.cdesc = cdesc
            get_class.save()
        except Exception as e:
            print e
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')


@login_required
def del_class(request):
    if request.method == 'POST':
        aid = request.POST['aid']
        get_cate = Cate.objects.get(aid=aid)
        get_cate.isdel = 1
        get_cate.save()
    return HttpResponseRedirect('/')


def get_all_api(request):
    try:
        aid = request.GET['aid']
        assert isinstance(int(aid), int)
        class_name = Cate.objects.get(aid=aid).cname
    except Exception as e:
        print e
        print "get_all_api_fail_1"
        return ""
    print "get_all_api - aid: {}".format(aid)
    all_api = Api.objects.filter(aid=aid).filter(isdel=0)
    return aid, all_api, class_name


@login_required
def class_detail(request):
    try:
        aid, all_api, class_name = get_all_api(request)
    except Exception as e:
        print e
        print "class_detail_fail_1"
        return HttpResponseRedirect('/')
    return render(request, 'cate_detail.html', locals())


@login_required
def copy_api(request):
    if request.method == "POST":
        api_id = request.POST["api_id"]
        api_name = request.POST["api_name"]
        api_object = Api.objects.get(id=int(api_id))
        api_object.id = None
        api_object.name = api_name
        api_object.save()
        return HttpResponse("success")


@login_required
def del_api(request):
    if request.method == "POST":
        api_id = request.POST["api_id"]
        api_object = Api.objects.get(id=int(api_id))
        api_object.isdel = 1
        api_object.save()
        return HttpResponse("success")


def get_create_update_arg(request):
    parameter = {}
    for i in request.POST:
        if i.startswith("param_"):
            """
                param_1_0 : username
                param_1_1 : int
            """
            # print i, request.POST[i].encode('utf-8')
            f1 = i.split('_')[1]
            f2 = i.split('_')[2]
            try:
                tmp = parameter[int(f2)]
            except Exception as e:
                tmp = {}
            tmp[int(f1)] = request.POST[i].strip()
            parameter[int(f2)] = tmp
        else:
            continue
            # print tmp
            # print parameter

    print "parameter: {}".format(parameter)

    kw = {
        "num": request.POST['num'].strip(),
        "url": request.POST['url'].strip(),
        "name": request.POST['name'].strip(),
        "des": request.POST['des'].strip(),
        "parameter": parameter,
        "memo": request.POST['memo'].strip(),
        "re": request.POST['re'].strip(),
        "type": request.POST['type'].strip(),
        "firstuid": request.user.id,
        "lastuid": request.user.id,
        "lasttime": int(time.time()),
    }
    return kw


@login_required
def edit_api(request):
    try:
        aid, all_api, class_name = get_all_api(request)
    except Exception as e:
        print e
        print "new_api_fail_1"
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))
    try:
        api_id = request.GET["id"]
    except Exception as e:
        print e
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))
    if request.method == "POST":
        kw = get_create_update_arg(request)
        kw['aid'] = aid
        del kw['firstuid']
        Api.objects.filter(id=api_id).update(**kw)
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))
    edit_api_object = Api.objects.get(id=int(api_id))
    return render(request, 'op_api.html', locals())


@login_required
def new_api(request):
    try:
        aid, all_api, class_name = get_all_api(request)
    except Exception as e:
        print e
        print "new_api_fail_1"
        return HttpResponseRedirect('/')

    if request.method == "POST":
        kw = get_create_update_arg(request)
        kw['aid'] = aid
        Api.objects.create(**kw)
        return HttpResponseRedirect('/class_detail/?aid={}'.format(aid))

    return render(request, 'op_api.html', locals())
