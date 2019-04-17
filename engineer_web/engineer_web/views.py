from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse, HttpResponseRedirect
from engineer.models import *
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('/login/')
    return inner


def login(request):
    # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        module = request.POST.get('module')
        user = None
        if module == 'UserInfo':
            user=UserInfo.objects.filter(username=username,password=password)
            print(user)
        elif module == 'Pic':
            user = Pic.objects.filter(pname=username,ppassword=password)
        elif module == 'SafeUser':
            user = SafeUser.objects.filter(sname=username,spassword=password)
        if user:
            #登录成功
            # 1，生成特殊字符串
            # 2，这个字符串当成key，此key在数据库的session表（在数据库存中一个表名是session的表）中对应一个value
            # 3，在响应中,用cookies保存这个key ,(即向浏览器写一个cookie,此cookies的值即是这个key特殊字符）
            request.session['is_login']='1'  # 这个session是用于后面访问每个页面（即调用每个视图函数时要用到，即判断是否已经登录，用此判断）
            # request.session['username']=username  # 这个要存储的session是用于后面，每个页面上要显示出来，登录状态的用户名用。
            # 说明：如果需要在页面上显示出来的用户信息太多（有时还有积分，姓名，年龄等信息），所以我们可以只用session保存user_id
            request.session['module'] = module
            request.session['user_id']=user[0].id
            if module == 'UserInfo':
                return redirect('/engineer/admin/')
            elif module == 'Pic':
                return redirect('/engineer/pic/')
            elif module == 'SafeUser':
                return redirect('/engineer/safeuser/')



    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return render(request,'engineer/login/login.html')



def index(request):
    # students=Students.objects.all()  ## 说明，objects.all()返回的是二维表，即一个列表，里面包含多个元组
    # return render(request,'index.html',{"students_list":students})
    # username1=request.session.get('username')
    user_id1=request.session.get('user_id')
    module = request.session.get('module')
    userobj = None
    picobj=None
    safeuserobj=None
    # 使用user_id去数据库中找到对应的user信息
    if module == 'UserInfo':
        userobj = UserInfo.objects.filter(id=user_id1)
        print(userobj)
    elif module=='Pic':
        picobj=Pic.objects.filter(id=user_id1)
    elif module=='SafeUser':
        safeuserobj = SafeUser.objects.filter(id=user_id1)
    if userobj:
        return {"user":userobj,'module':module}
    elif picobj:
        return {'user':picobj,'module':module}
    elif safeuserobj:
        return {'user':safeuserobj,'module':module}

# 退出登录
# @login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")


# 注册功能
@check_login
def regist(request):
    userinfoList=UserInfo.objects.all()
    return render(request,'engineer/login/regist.html',{'userinfoList':userinfoList})