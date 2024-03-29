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

    #添加逻辑 用cartid索引索引数据 而不是pid
    product['pid']=pid

    #尝试获取购物车sessiong
    cartlist=request.session.get('cartlist',{})
    #获取小料sessgion
    materials= request.session.get('materials',{})
    print(materials)

    # 把菜放进购物车
    cartid=len(cartlist)+1
    cartlist[cartid] = product
    # if pid in cartlist:
    #     cartlist[pid]['num']+=product['num']
    # else:
    #     cartlist[pid]=product

    #materials添加cartid值
    for mItem in materials:
        mItem["cartid"]=cartid

    #放入productlist的produc里面
    product['materials']=materials
    if materials!= {}:
        del request.session['materials']
        print(product['materials'])


    #讲cartlist放入购物车
    request.session['cartlist']=cartlist
    #print((cartlist))
    return redirect("web_index")
def delete(request,cartid):
    """删除购物车"""
    # 从session中获取当前店铺中的所以菜品信息
    cartlist=request.session.get('cartlist',{})
    del cartlist[cartid]
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
    cartid=request.GET.get("cartid",0)
    m=int(request.GET.get('num',1))

    print(m)
    if m<1:
        m=1

    #改为cartid
    cartlist[cartid]['num']=m


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