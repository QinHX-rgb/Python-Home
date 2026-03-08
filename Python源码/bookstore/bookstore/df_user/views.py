from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from hashlib import sha1
from df_user.models import *
from df_goods.models import *
from df_order.models import OrderInfo
from django.core.paginator import Paginator

from PIL import Image, ImageDraw, ImageFont
import random

# 判断用户是否登录的装饰器
def islogin(func):
    def login_func(request, *args, **kwargs):
        # 判断是否登录
        if request.session.get('user_id'):
            # 用户已经登录 可以正常访问页面
            return func(request, *args, **kwargs)
        else:
            # 用户未登录 跳转到登录页面
            red = HttpResponseRedirect('/user/login')
            # 获取用户尝试访问的路径
            path = request.get_full_path()
            # 把该路径存到cookie中
            red.set_cookie('url', path)
            return red
    return login_func


# Create your views here.
def register(request):
    context = {'title': '天天书城-注册'}
    return render(request, 'df_user/register.html', context)

def register_handle(request):
    # 获取用户输入的内容
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    # 判断两次输入的密码是否一致
    # if upwd != ucpwd:
    #     return HttpResponseRedirect('/user/register')

    # 对密码原文进行sha1的加密
    # 创建sha1对象
    s1 = sha1()
    # 对password进行sha1的加密
    s1.update(upwd.encode())
    upwd2 = s1.hexdigest()
    # print(upwd2)

    # 把用户信息存入数据库
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd2
    user.uemail = uemail
    user.save()

    return HttpResponseRedirect('/user/login')

def register_exist(request):
    # 接收用户传入的uname参数
    get = request.GET
    uname = get.get('uname')
    # 在数据库中查询该用户是否存在
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})

def verifyCode(request):
    # 指定画布的宽度
    width = 100
    height = 25
    # 指定背景色
    bgColor = (64, 64, 64)  # 较深

    # 创建画布
    # 参数1 mode 模式
    # 参数2 size 画布的大小 是一个长度为2的元组
    # 参数3 color 画布的背景色 是一个长度为3的元组 (RGB)
    image = Image.new('RGB', (width, height), bgColor)
    # 创建画笔
    # 参数1 im 画布对象
    # 参数2 mode 模式 默认为None
    draw = ImageDraw.Draw(image)
    # 创建字体
    # 参数1 font 字体文件
    # 参数2 字体大小
    font = ImageFont.truetype('D:\FreeMono.ttf', 24)
    # 文字
    text = '0123456789'
    textTemp = ''
    # 在画布上逐个描字符
    for i in range(4):

        textTemp1 = text[random.randrange(0, 10)]
        textTemp += textTemp1
        # 使用画笔在画布上绘制字符
        # 参数1 xy 要描述的字符左上角的坐标 长度为2的元组
        # 参数2 text 要描述的字符
        # 参数3 fill 要描述的字符的颜色
        # 参数4 font 字体
        draw.text((25 * i, 0), textTemp1, (255, 255, 255), font)

    request.session['code'] = textTemp
    # 把画布保存到内存中
    import io
    buf = io.BytesIO()
    image.save(buf, 'png')

    return HttpResponse(buf.getvalue(), 'image/png')

def verifyTest(request):
    return render(request, 'df_user/login.html')

def verifyTest2(request):
    sessionCode = request.session['code']
    postCode = request.POST['code']

    if sessionCode == postCode:
        return HttpResponse('ok')
    else:
        return HttpResponse('fail')

def login(request):
    context = {'title': '天天书城-登录', 'error_name': 0, 'error_pwd': 0}
    return render(request, 'df_user/login.html', context)

def login_handle(request):

    # 获取用户输入的信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu')
    code = post.get('code')

    textTemp = request.session.get('code')
    if code != textTemp:
        context = {'code_error': 1, }
        return render(request, 'df_user/login.html', context)

    # 根据用户名和密码查询数据库
    users = UserInfo.objects.filter(uname=uname)
    if len(users) > 0:
        # 用户存在
        # 对密码原文进行sha1的加密
        s1 = sha1()
        s1.update(upwd.encode())
        upwd2 = s1.hexdigest()

        # 与数据库中的密文进行比较
        if upwd2 == users[0].upwd:
            # 登录成功
            # 从cookie中提取之前保存好的路径
            url = request.COOKIES.get('url', '/user/info')
            red = HttpResponseRedirect(url)
            if jizhu:
                red.set_cookie('uname', uname)  # 记住用户名
            else:
                red.set_cookie('uname', '')  # 没有记住用户名
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red

        else:  # 密码错误的情况
            context = {'title': '登录', 'error_name': 0, 'error_pwd': 1,
                       'uname': uname, 'upwd': upwd, }

            return render(request, 'df_user/login.html', context)

    else:  # 用户不存在的情况
        context = {'title': '登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd, }
        return render(request, 'df_user/login.html', context)


@islogin
def info(request):
    # 读取数据库中的用户信息
    user = UserInfo.objects.get(id=request.session['user_id'])
    user_name = user.uname
    user_address = user.uaddress
    user_phone = user.uphone

    # 从cookies中读取最近浏览的信息
    goods_ids = request.COOKIES.get('goods_ids')
    # 判断cookie中的最近浏览商品序列是否为空
    if goods_ids and goods_ids != '':
        # 不为空 以逗号分隔
        goods_ids = goods_ids.split(',')
    else:
        # 为空
        goods_ids = []

    # 根据goods_ids中商品的id 去数据库中查询 找出商品对象


    goods_list = []
    for id in goods_ids:
        goods = GoodsInfo.objects.get(id=id)
        goods_list.append(goods)

    context = {'title': '天天书城-用户中心',
               'user_name': user_name,
               'user_address': user_address,
               'user_phone': user_phone,
               'info': 1,
               'goods_list': goods_list}
    return render(request, 'df_user/user_center_info.html', context)

@islogin
def order(request, pageid):
    if pageid == '': pageid = 1
    pageid = int(pageid)
    ''' 展示用户提交的订单 由购物车页面下单后跳转过来 也可以由个人信息页面随时查看 根据用户订单是否支付 下单顺序进行排序 '''
    uid = request.session.get('user_id')
    orderinfos = OrderInfo.objects.filter(user_id=uid).order_by('oIsPay','-oid')
    # 分页
    paginator = Paginator(orderinfos, 2)
    orderlist = paginator.page(pageid)
    plist = paginator.page_range
    context = {'title': '用户中心', 'order': 1, 'user_center': 1, 'pageid': pageid, 'orderlist': orderlist, 'plist': plist}
    return render(request, 'df_user/user_center_order.html', context)

@islogin
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        print(jcc)
hcjhhiinh


