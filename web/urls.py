"""
URL configuration for csos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from web.views import index

urlpatterns = [
    path("", index.index, name="index"),

    #前端登录退出的路由
    path('login',index.login,name="web_login"),
    path('login',index.dologin,name='web_dologin'),
    path('logout',index.logout,name='web_logout'),
    #验证码: 不打算做path('verify',index.verify,name='web_verify')


    #为URL路由器添加请求前缀 web/反是带web前缀的 才进行
    path("web/",include([
        path("", index.webindex, name="web_index"), #前台大堂点餐首页
    ]))
]
