
import json

from django.core.serializers import serialize
from django.db.models import Q

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from myadmin.models import User, Category, Product, Member,Batchings

def show(request):
    oba=Batchings.objects.filter(status=1)
    context={"materials":oba}

    return render(request,"web/batching.html",context)