
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
