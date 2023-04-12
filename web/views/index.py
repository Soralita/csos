from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from myadmin.models import User, Category, Product


# Create your views here.

def index(request):
    """项目前台大堂点餐首页"""
    return redirect(reverse("web_index"))

def webindex(request):
    """项目前台大堂点餐首页"""


    #购物车金额
    cartlist=request.session.get('cartlist',{})
    total_money=0
    for vo in cartlist.values():
        total_money+=vo['num']*vo['price']
    request.session['total_money']=total_money


    context={'categorylist':request.session.get("categorylist",{}).items()}
    return render(request,"web/index.html",context)

def login(request):

    return render(request,"web/login.html")


def dologin(request):
    try:
        # 执行验证码的校验
        # if request.POST['code'] != request.session['verifycode']:
        #     context = {"info": "验证码错误！"}
        #     return render(request, "myadmin/index/login.html", context)

        # 根据登录账号获取登录者信息
        user = User.objects.get(username=request.POST['username'])
        # 判断当前用户是否是管理员
        if user.status == 6 or user.status ==1:
            # 判断登录密码是否相同
            import hashlib
            md5 = hashlib.md5()
            s = request.POST['pass'] + user.password_salt  # 从表单中获取密码并添加干扰值
            md5.update(s.encode('utf-8'))  # 将要产生md5的子串放进去
            if  user.password_hash == md5.hexdigest():  # 获取md5值
                print('登录成功')
                # 将当前登录成功的用户信息以adminuser为key写入到session中
                request.session['webuser'] = user.toDict()

                try:
                    #获取菜品类别和菜品行信息
                    clist=Category.objects.filter(status=1)
                    #print(clist)
                    categorylist=dict()
                    productlist=dict()
                    for vo in clist:
                        c={'id':vo.id,'name':vo.name,'pids':[]}

                        plist=Product.objects.filter(category_id=vo.id,status=1)

                        for p in plist:
                            c['pids'].append(p.toDict())
                            productlist[p.id]=p.toDict()
                        categorylist[vo.id]=c

                    #将上面的结果存入session中
                    request.session['categorylist']=categorylist
                    request.session['productlist']=productlist
                except Exception as err:
                    print(err+"获取菜品类别错误")

                # 重定向到后台管理首页
                return redirect(reverse("web_index"))
            else:
                return redirect(reverse("web_login")+"?errinfo=5")
        else:
            return redirect(reverse("web_login")+"?errinfo=4")
    except Exception as err:
        print(err)
        return redirect(reverse("web_login")+"?errinfo=3")


def logout(request):
    del request.session['webuser']
    return redirect(reverse('web_login'))

def verify(request):
    pass

