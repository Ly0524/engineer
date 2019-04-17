from django.contrib import admin
from django.urls import path,include
from engineer_web.views import *

urlpatterns = [
    path('regist/',regist),
    path('admin/', admin.site.urls),
    path('login/',login),
    path('index/',index),
    path('logout/',logout),
    path('engineer/',include(('engineer.urls','engineer'),namespace='engineer')),

]
