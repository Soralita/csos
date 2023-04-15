#会员信息管理的视图文件
import pytz as pytz
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import datetime
# Create your views here.
from myadmin.models import Member

def index(request,pIndex=1):
    '''浏览信息'''
    umod = Member.objects
    ulist = umod.filter(status__lt=9)
    mywhere=[]
    #判断并处理状态搜索条件
    status = request.GET.get('status','')
    if status != '':
        ulist = ulist.filter(status=status)
        mywhere.append("status="+status)


    # 获取并判断搜索条件
    kw = request.GET.get("keyword", None)
    if kw:
        ulist = ulist.filter(Q(nickname__contains=kw) | Q(mobile__contains=kw))
        mywhere.append('keyword=' + kw)



    ulist = ulist.order_by("id")#对id排序
    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(ulist,10) #以每页5条数据分页
    maxpages = page.num_pages #获取最大页数
    #判断当前页是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #获取当前页数据
    plist = page.page_range #获取页码列表信息

    # 计算会员时间
    for vo in list2:
        if vo.level ==2 and vo.expiration_at!=None:
            # vo.levelDay=(datetime.strptime(vo.expiration_at,'%Y-%m-%d %H:%M:%S')-datetime.now()).days
            now=datetime.now()
            now=now.replace(tzinfo=pytz.timezone("Asia/Shanghai"))
            vo.levelDay=(vo.expiration_at-now).days
        else:
            vo.levelDay=None




    context = {"memberlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myadmin/member/index.html",context)

def delete(request,mid=0):
    '''执行信息删除'''
    try:
        ob = Member.objects.get(id=mid)
        ob.status = 9
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"删除成功！"}
    except Exception as err:
        print(err)
        context = {'info':"删除失败！"}
    return render(request,"myadmin/info.html",context)


def edit(request,mid=0):
    '''加载信息编辑表单'''
    try:
        om = Member.objects.get(id=mid)
        context = {'member': om}
        return render(request, "myadmin/member/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': "没有找到要修改的信息！"}
        return render(request, "myadmin/info.html", context)
def update(request, mid):
    '''执行信息编辑'''
    try:
        om = Member.objects.get(id=mid)
        om.nickname = request.POST['nickname']
        om.mobile = request.POST['mobile']
        om.level = request.POST['level']

        # 将request.POST['expirationAt'] date格式赋值给datetime格式的om.expiration
        if om.level=="2" or om.level==2:
            om.expiration_at=datetime.strptime(request.POST['expirationAt'],"%Y-%m-%d").strftime("%Y-%m-%d")
            #print(om.expiration_at)
        om.credit=request.POST['credit']
        om.status = request.POST['status']
        om.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        om.save()
        context = {'info': "修改成功！"}
    except Exception as err:
        print(err)
        context = {'info': "修改失败！"}
    return render(request, "myadmin/info.html", context)


def add(request):
    '''加载信息添加表单'''
    return render(request, "myadmin/member/add.html")


def insert(request):
    '''执行信息添加'''
    try:
        om = Member()
        om.nickname = request.POST['nickname']
        om.mobile = request.POST['mobile']
        om.level = request.POST['level']

        # 将request.POST['expirationAt'] date格式赋值给datetime格式的om.expiration
        if om.level == "2" or om.level == 2:
            om.expiration_at = datetime.strptime(request.POST['expirationAt'], "%Y-%m-%d").strftime("%Y-%m-%d")
            # print(om.expiration_at)
        om.credit = 0
        om.status = 1
        om.avatar="moren.png"

        om.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        om.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        om.save()
        context = {'info': "添加成功！"}
    except Exception as err:
        print(err)
        context = {'info': "添加失败！"}
    return render(request, "myadmin/info.html", context)
