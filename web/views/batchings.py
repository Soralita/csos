
import json

from django.core.serializers import serialize
from django.db.models import Q

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from myadmin.models import User, Category, Product, Member,Batchings
from web.views import cart


def show(request):
    oba=Batchings.objects.filter(status=1)
    pid=request.GET.get("pid",0)
    context={"materials":oba,"pid":pid}
    return render(request,"web/batching.html",context)

def buy(request):
    if request.method == 'POST':
        materials = request.POST.get('materials', '[]')
        pid=request.POST.get('pid',0)
        print("met"+materials+"pid"+pid)

        try:
            materials = json.loads(materials)
        except ValueError:
            materials = []

        if isinstance(materials, list):
            # 将购买信息存储到 Session 中
            request.session['materials'] = materials

            #向购物车添加请求
            try:
                cart.add(request,pid)
            except Exception as err:
                print(err)
                return JsonResponse({'success': False})

            return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def change(request):
    """更改购物车"""
    cartlist=request.session.get('cartlist',{})
    bid=request.GET.get("bid",0)
    cartid=request.GET.get("cartid",0)
    m=int(request.GET.get('num',1))

    print(m)
    if m<1:
        m=1

    for vo in cartlist[cartid]['materials']:
        if vo['id']==int(bid):
            vo['quantity']=int(m)
            print("m"+str(m))
            print(vo)
            break


    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))

def delete(request,cart_id,batching_id):
    cartlist = request.session.get('cartlist', {})
    # print(cart_id,type(cart_id))
    # print(batching_id,type(batching_id))
    # print(cartlist[cart_id]['materials'])

    cartlist[cart_id]['materials']=[b for b in cartlist[cart_id]['materials'] if b['id']!=int(batching_id)]
    request.session['cartlist'] = cartlist
    return redirect(reverse('web_index'))

