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

from web.views import index, orders, batchings
from web.views import cart

urlpatterns = [
    path("", index.index, name="index"),

    #前端登录退出的路由
    path('login',index.login,name="web_login"),
    path('dologin',index.dologin,name='web_dologin'),
    path('logout',index.logout,name='web_logout'),
    #验证码: 不打算做path('verify',index.verify,name='web_verify')


    #为URL路由器添加请求前缀 web/反是带web前缀的 才进行
    path("web/",include([
        path("", index.webindex, name="web_index"), #前台大堂点餐首页
        #购物车视图
        path('cart/add/<str:pid>',cart.add,name="web_cart_add"),
        path('cart/delete/<str:cartid>',cart.delete,name="web_cart_delete"),
        path('cart/clear',cart.clear,name="web_cart_clear"),
        path('cart/change',cart.change,name="web_cart_change"),

        path('cart/member', cart.member, name='web_cart_member'),

        #订单处理路由
        path('orders/<int:pIndex>',orders.index,name='web_orders_index'),
        path('orders/insert',orders.insert,name='web_orders_insert'),
        path('orders/detail',orders.detail,name='web_orders_detail'),
        path('orders/status',orders.status,name='web_orders_status'),
        path('orders/speak',orders.speak,name='web_orders_speak'),
        path('orders/orderSpeak',orders.orderSpeak,name='web_orders_orderSpeak'),

        #小料处理
        path('batching/show',batchings.show,name='web_batchings_show'),
        path('batching/buy',batchings.buy,name='web_batchings_buy'),
        path('batching/change',batchings.change,name='web_batchings_change'),
        path('batching/delete/<str:cart_id>/<int:batching_id>/',batchings.delete,name='web_batchings_delete'),

    ]))
]
