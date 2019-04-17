from django.urls import re_path,path
from .views import *


urlpatterns = [

    path('admin/',admin),
    path('show_admin/',show_admin),
    path('add_admin/',add_admin),
    re_path('admin/(\d+?)/change/',change_admin),
    re_path('admin/(\d+?)/delete/',delete_admin),

    path('pic/',pic),
    path('show_pic/', show_pic),
    path('add_pic/',add_pic),
    re_path('pic/(\d+?)/change/', change_pic),
    re_path('pic/(\d+?)/delete/',delete_pic),

    path('safeuser/',safeuser),
    path('show_safeuser/',show_safeuser),
    path('add_safeuser/',add_safeuser),
    re_path('safeuser/(\d+?)/change/', change_safeuser),
    re_path('safeuser/(\d+?)/delete/',delete_safeuser),

    path('show_work/',show_work),
    path('add_work/',add_work),
    re_path('work/(\d+?)/change/', change_work),
    re_path('work/(\d+?)/delete/',delete_work),

    path('show_notifyinfo/',show_notifyinfo),
    re_path('notifyinfo/(\d+?)/change/', change_notifyinfo),



]