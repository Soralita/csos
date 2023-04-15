import json

from django.core.serializers import serialize
from django.db.models import Q

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from myadmin.models import User, Category, Product, Member


# Create your views here.

def add(request,pid):
    """添加购物车"""
    #从session中获取当前店铺中的所以菜品信息
    product=request.session['productlist'][pid]
    product['num']=1 #初始化

    #尝试获取购物车sessiong
    cartlist=request.session.get('cartlist',{})
    # 把菜放进购物车
    if pid in cartlist:
        cartlist[pid]['num']+=product['num']
    else:
        cartlist[pid]=product
    #讲cartlist放入购物车
    request.session['cartlist']=cartlist
    #print((cartlist))
    return redirect("web_index")
def delete(request,pid):
    """删除购物车"""
    # 从session中获取当前店铺中的所以菜品信息
    cartlist=request.session.get('cartlist',{})
    del cartlist[pid]
    request.session['cartlist']=cartlist
    return redirect(reverse('web_index'))

def clear(request):
    """清空购物车"""
    request.session['cartlist'] = {}
    return redirect(reverse('web_index'))


def change(request):
    """更改购物车"""
    cartlist=request.session.get('cartlist',{})
    pid=request.GET.get("pid",0)
    m=int(request.GET.get('num',1))
    print(m)
    if m<1:
        m=1
    cartlist[pid]['num']=m

    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))


def member(request):
    """加载订单详情"""
    kw=request.GET.get("keyword","")

    om=Member.objects
    mlist = om.filter(Q(nickname__contains=kw) | Q(mobile__contains=kw))
    mlist = mlist.order_by("id")  # 对id排序

    context = {"memberlist": mlist}
    return render(request, "web/orderMember.html", context)