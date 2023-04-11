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
from django.urls import path

from myadmin.views import index, user, category, product, member

urlpatterns = [
    path("", index.index,name="myadmin_index"),

    # 员工信息管理路由
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),  # 浏览
    path('user/add', user.add, name="myadmin_user_add"),  # 添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),  # 执行添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_delete"),  # 执行删除
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),  # 加载编辑表单
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # 执行编辑

    # 后台管理员登录、退出路由
    path('login', index.login, name="myadmin_login"),  # 加载登录表单
    path('dologin', index.dologin, name="myadmin_dologin"),  # 执行登录
    path('logout', index.logout, name="myadmin_logout"),  # 退出
    path('verify', index.verify, name="myadmin_verify"),  # 输出验证码

    # 菜品类别信息管理路由
    path('category/<int:pIndex>', category.index, name="myadmin_category_index"),  # 浏览
    path('category/load/<int:sid>', category.loadCategory, name="myadmin_category_load"),
    path('category/add', category.add, name="myadmin_category_add"),  # 添加表单
    path('category/insert', category.insert, name="myadmin_category_insert"),  # 执行添加
    path('category/del/<int:cid>', category.delete, name="myadmin_category_del"),  # 执行删除
    path('category/edit/<int:cid>', category.edit, name="myadmin_category_edit"),  # 加载编辑表单
    path('category/update/<int:cid>', category.update, name="myadmin_category_update"),  # 执行编辑

    # 菜品信息管理路由
    path('product/<int:pIndex>', product.index, name="myadmin_product_index"),  # 浏览
    path('product/add', product.add, name="myadmin_product_add"),  # 添加表单
    path('product/insert', product.insert, name="myadmin_product_insert"),  # 执行添加
    path('product/del/<int:pid>', product.delete, name="myadmin_product_del"),  # 执行删除
    path('product/edit/<int:pid>', product.edit, name="myadmin_product_edit"),  # 加载编辑表单
    path('product/update/<int:pid>', product.update, name="myadmin_product_update"),  # 执行编辑

    #会员信息管理路由
    path('member/<int:pIndex>', member.index, name="myadmin_member_index"), #浏览
]
