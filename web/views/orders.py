import concurrent
import os
import subprocess
import sys

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from datetime import time, datetime

from myadmin.models import Orders, OrderDetail, Product, Payment,BatchingDetail

from myadmin.models import User, Category, Product

from csos.utils import queuing
from web.views.payment import pay_qrcode, pay_trade


# Create your views here.

def index(request,pIndex=1):
    '''浏览信息'''
    umod = Orders.objects
    mywhere = []
    # 获取并判断搜索条件
    # 获取、判断并封装状态status搜索条件
    status = request.GET.get('status', '')
    if status != '':
        ulist = umod.filter(status=status)
        mywhere.append("status=" + status)
    else:
        ulist=umod

    ulist = ulist.order_by("id")  # 对id排序

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist, 10)  # 以每页5条数据分页
    maxpages = page.num_pages  # 获取最大页数
    # 判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 获取当前页数据
    plist = page.page_range  # 获取页码列表信息

    for vo in list2:
        if vo.user_id ==0:
            vo.nickname='无'
        else:
            #单独字段的查询
            user=User.objects.only('nickname').get(id=vo.user_id)
            vo.nickname=user.nickname


    context = {"orderslist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "web/list.html", context)


def insert(request):
    """执行订单添加"""

    try:
        #订单添加
        # 查询当天订单的数聊
        now = datetime.now().date()
        todayList=Orders.objects.filter(create_at__gt=now)
        flow_num=len(todayList)+1
        if flow_num>200:
            flow_num=flow_num-200

        od = Orders()
        # 获取member

        member_id=request.GET.get("mid",0)

        od.member_id=member_id
        od.user_id=request.session['webuser']['id']
        od.money=request.session['total_money']
        od.status = 1#订单状态:1过行中/2无效/3已完成
        od.payment_status = 2    # 支付状态:1未支付/2已支付/3已退款
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.flow_num=flow_num
        od.save()

        #执行支付信息添加
        op=Payment()
        op.order_id=od.id #订单id号
        op.member_id =member_id
        op.type = 2 #1 会员付款2收应援收款
        op.bank = request.GET.get('bank',3) #收款渠道 1:微信/2:余额/3:现金/4:支付宝
        op.money=request.session['total_money']
        op.status = 2 #支付状态
        op.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        # pay_qrcode(op)
        pay_trade(op)

        #执行订单详情添加
        cartlist = request.session.get('cartlist',{})
        for item in cartlist.values():
            ov=OrderDetail()
            ov.order_id = od.id  # 订单id
            ov.product_id = item['pid']  # 菜品id
            ov.product_name = item['name']  # 菜品名称
            ov.price = item['price'] # 单价
            ov.quantity = item['num']  # 数量
            ov.status = 1 # 状态:1正常/9删除
            ov.save()

        #执行小料详情添加
        for item in cartlist.values():
            materials=item['materials']

            for materItem in materials:
                # print(type(materItem))
                oba = BatchingDetail()
                oba.batching_id=materItem['id']
                oba.order_d_id=od.id
                oba.product_id=item['id']
                oba.batching_name=materItem['name']
                oba.batching_price=materItem['price']
                oba.quantity=materItem['quantity']
                oba.cartid=materItem["cartid"]
                oba.save()




        del request.session['cartlist']
        del request.session['total_money']

        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return HttpResponse("N")

def detail(request):
    """加载订单详情"""
    oid=request.GET.get("oid",0)
    dlist=OrderDetail.objects.filter(order_id=oid)
    context={"detaillist":dlist}
    return render(request,"web/detail.html",context)

def orderSpeak(request):
    """加载订单详情"""
    umod = Orders.objects
    ulist=umod.filter(status=1)
    #添加当天订单叫号条件
    now = datetime.now().date()
    ulist = ulist.filter(create_at__gt=now)

    ulist = ulist.order_by("id")  # 对id排序
    context = {"orderslist": ulist}
    return render(request, "web/orderSpeak.html", context)

#快速排序算法

def status(request):
    try:
        oid=request.GET.get("oid",0)
        ob=Orders.objects.get(id=oid)
        ob.status=request.GET["status"]
        ob.save()
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return HttpResponse("N")

def speak(request):
    from csos.settings import SPEAK_PY_FILE,STATIC_AUDIO_FILE
    try:
        flow_num = request.GET.get("flow_num",-1)
        if flow_num!=-1:
            #线程池
            # print(flow_num)
            # with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            #     future = executor.submit(queuing.play_audio,flow_num)
            #     print(future.result())
            filepath=os.path.join(STATIC_AUDIO_FILE,str(flow_num)+".wav")
            subprocess.Popen([sys.executable,SPEAK_PY_FILE,filepath],stdin = subprocess.PIPE, stdout=subprocess.PIPE)
            # queuing.play_audio(flow_num)
        else:
            return HttpResponse("N")
        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return HttpResponse("N")

