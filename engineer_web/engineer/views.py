from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.views.generic.base import View

from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from engineer_web.views import check_login, index
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


# @csrf_exempt
# class Page(View):
#     def __init__(self,name,html):
#         super(Page, self).__init__(name,html)
#         self.name=name
#         self.html=html
#
#     @check_login
#     def show(name,html, request):
#         userinfoList = name.objects.all()
#         paginator = Paginator(userinfoList, 2)
#         dic = index(request)
#         if request.method == 'GET':
#             num = request.GET.get('page')
#             try:
#                 number = paginator.page(num)
#             except PageNotAnInteger:
#                 number = paginator.page(1)
#             except InvalidPage:
#                 return HttpResponse('找不到页面的内容')
#             except EmptyPage:
#                 number = paginator.page(paginator.num_pages)
#
#         return render(request, html, {'page': number, 'paginator': paginator
#             , "userinfoList": number, 'user': dic['user'], 'module': dic['module']})


# 管理员视图
@check_login
def admin(request):
    dic = index(request)
    return render(request, 'engineer/admin/admin.html', {'user': dic['user'], 'module': dic['module']})


@check_login
def show_admin(request):
    userinfoList = UserInfo.objects.all()
    paginator = Paginator(userinfoList, 2, 3)
    dic = index(request)
    if request.method == 'GET':
        num = request.GET.get('page')
        try:
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            number = paginator.page(paginator.num_pages)

    return render(request, 'engineer/admin/show_admin.html', {'page': number, 'paginator': paginator
        , "userinfoList": number, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def add_admin(request):
    dic = index(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = UserInfo
        obj = user(username=username, password=password)
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_admin/')
    return render(request, 'engineer/admin/add_admin.html', {'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def change_admin(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        obj = UserInfo.objects.get(id=id)
        obj.username = username
        obj.password = password
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_admin/')
    userinfoList = UserInfo.objects.get(id=id)
    return render(request, 'engineer/admin/change_admin.html',
                  {'userinfoList': userinfoList, 'id': id, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def delete_admin(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        UserInfo.objects.filter(id=id).delete()

        return redirect('/engineer/show_admin/')

    return render(request, 'engineer/admin/delete_admin.html', {'id': id, 'user': dic['user'], 'module': dic['module']})


# 负责人视图
@check_login
def pic(request):
    dic=index(request)
    return render(request,'engineer/pic/pic.html',{'user': dic['user'], 'module': dic['module']})

@csrf_exempt
@check_login
def show_pic(request):
    picList = Pic.objects.all()
    paginator = Paginator(picList, 2,3)
    dic = index(request)
    if request.method == 'GET':
        num = request.GET.get('page')
        try:
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
    return render(request, 'engineer/pic/show_pic.html', {'page': number, 'paginator': paginator
        , "picList": number, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def add_pic(request):
    dic = index(request)
    if request.method == 'POST':
        pname = request.POST['pname']
        ppassword = request.POST['ppassword']
        pinstitute = request.POST['pinstitute']

        user = Pic
        obj = user(pname=pname, ppassword=ppassword, pinstitute=pinstitute)
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_pic/')
    return render(request, 'engineer/pic/add_pic.html', {'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def change_pic(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        pname = request.POST['pname']
        ppassword = request.POST['ppassword']
        pinstitute = request.POST['pinstitute']

        obj = Pic.objects.get(id=id)
        obj.pname = pname
        obj.ppassword = ppassword
        obj.pinstitute = pinstitute
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_pic/')
    picList = Pic.objects.get(id=id)
    return render(request, 'engineer/pic/change_pic.html',
                  {'picList': picList, 'id': id, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def delete_pic(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        Pic.objects.filter(id=id).delete()

        return redirect('/engineer/show_pic/')

    return render(request, 'engineer/pic/delete_pic.html', {'id': id, 'user': dic['user'], 'module': dic['module']})


# 安全员视图

@check_login
def safeuser(request):
    dic=index(request)
    return render(request,'engineer/safeuser/safeuser.html',{'user': dic['user'], 'module': dic['module']})

@check_login
def show_safeuser(request):
    safeuserList = SafeUser.objects.all()
    paginator = Paginator(safeuserList, 4)
    dic = index(request)
    if request.method == 'GET':
        num = request.GET.get('page')
        try:
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
    return render(request, 'engineer/safeuser/show_safeuser.html', {'page': number, 'paginator': paginator
        , "safeuserList": number, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def add_safeuser(request):
    dic = index(request)
    if request.method == 'POST':
        username = request.POST['sname']
        password = request.POST['spassword']
        institute = request.POST['sinstitute']
        p = request.POST['p']
        p = int(p)

        user = SafeUser
        obj = user(sname=username, spassword=password, sinstitute=institute, p_id=p)
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_safeuser/')
    picList = Pic.objects.all()
    return render(request, 'engineer/safeuser/add_safeuser.html',
                  {'picList': picList, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
@check_login
def change_safeuser(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        sname = request.POST['sname']
        spassword = request.POST['spassword']
        sinstitute = request.POST['sinstitute']
        p = request.POST['p']
        p = int(p)

        obj = SafeUser.objects.get(id=id)
        obj.sname = sname
        obj.spassword = spassword
        obj.sinstitute = sinstitute
        obj.p_id = p
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_safeuser/')
    picList = Pic.objects.all()
    safeuserList = SafeUser.objects.get(id=id)
    return render(request, 'engineer/safeuser/change_safeuser.html',
                  {'picList': picList, 'safeuserList': safeuserList, 'id': id, 'user': dic['user'],
                   'module': dic['module']})


@csrf_exempt
@check_login
def delete_safeuser(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        SafeUser.objects.filter(id=id).delete()

        return redirect('/engineer/show_safeuser/')

    return render(request, 'engineer/safeuser/delete_safeuser.html',
                  {'id': id, 'user': dic['user'], 'module': dic['module']})


# 工地视图
def show_work(request):
    workList = Work.objects.all()
    paginator = Paginator(workList, 4)
    dic = index(request)
    if request.method == 'GET':
        num = request.GET.get('page')
        try:
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
    return render(request, 'engineer/work/show_work.html', {'page': number, 'paginator': paginator
        , "workList": number, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
def add_work(request):
    dic = index(request)
    if request.method == 'POST':
        wengineer_name = request.POST['wengineer_name']
        wengineer_num = request.POST['wengineer_num']
        wlinkman = request.POST['wlinkman']
        wphone = request.POST['wphone']

        user = Work
        obj = user(wengineer_name=wengineer_name, wengineer_num=wengineer_num, wlinkman=wlinkman, wphone=wphone)
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_work/')
    workList = Work.objects.all()
    return render(request, 'engineer/work/add_work.html',
                  {'workList': workList, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
def change_work(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        wengineer_name = request.POST['wengineer_name']
        wengineer_num = request.POST['wengineer_num']
        wlinkman = request.POST['wlinkman']
        wphone = request.POST['wphone']

        obj = Work.objects.get(id=id)
        obj.wengineer_name = wengineer_name
        obj.wengineer_num = wengineer_num
        obj.wlinkman = wlinkman
        obj.wphone = wphone
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_work/')
    workList = Work.objects.get(id=id)

    return render(request, 'engineer/work/change_work.html',
                  {'workList': workList, 'id': id, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
def delete_work(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        Work.objects.filter(id=id).delete()

        return redirect('/engineer/show_work/')

    return render(request, 'engineer/work/delete_work.html', {'id': id, 'user': dic['user'], 'module': dic['module']})


# 通知信息视图
def show_notifyinfo(request):

    notifyList = NotifyInfo.objects.all()
    safeList = SafeUser.objects.all()
    workList = Work.objects.all()
    paginator = Paginator(notifyList, 4)
    dic = index(request)
    if request.method == 'GET':
        num = request.GET.get('page')
        try:
            number = paginator.page(num)
        except PageNotAnInteger:
            number = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            number = paginator.page(paginator.num_pages)
    return render(request, 'engineer/notifyinfo/show_notify.html', {'page': number, 'paginator': paginator
        , "notifyList": number,'safeList': safeList, 'workList': workList, 'user': dic['user'], 'module': dic['module']})


@csrf_exempt
def change_notifyinfo(request, id):
    dic = index(request)
    id = int(id)
    if request.method == 'POST':
        # errortype = request.POST['errortype']
        dealvalue = request.POST['dealvalue']
        # safe_id=request.POST['s']
        # safe_name=request.POST['s_name']
        # work_id=request.POST['w']
        # createTime = request.POST['createTime']
        # changTime = request.POST['changeTime']

        obj = NotifyInfo.objects.get(id=id)
        # obj.errortype = errortype
        obj.dealvalue = dealvalue
        # obj.s = safe_id
        # obj.w = work_id
        try:
            obj.save()
        except:
            print('保存失败！')
        return redirect('/engineer/show_notifyinfo/')
    notifyList = NotifyInfo.objects.get(id=id)
    safeList = SafeUser.objects.get(id=id)
    workList = Work.objects.get(id=id)

    return render(request, 'engineer/notifyinfo/change_notify.html',
                  {'safeList': safeList, 'workList': workList, 'notifyList': notifyList, 'id': id, 'user': dic['user'],
                   'module': dic['module']})

