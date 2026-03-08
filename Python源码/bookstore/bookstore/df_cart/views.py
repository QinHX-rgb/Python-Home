from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
from df_cart.models import CartInfo

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


@islogin
def cart(request):
    # 从session中获取当前用户的id
    uid = request.session.get('user_id')
    # 根据id搜索当前用户放入购物车中的品种
    carts = CartInfo.objects.filter(user_id=uid)

    context = {'title': '天天生鲜-购物车',
               'carts': carts}

    return render(request, 'df_cart/cart.html', context)


def add(request, gid, count):
    # 从session中获取用户id
    uid = request.session.get('user_id')
    count = int(count)  # 字符串转整数

    # 从数据库中根据uid和gid读取商品数量
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)  # carts的数量要么是0(没有) 要么是1(有)
    if len(carts) >= 1:
        # 购物车中已经有商品
        cart = carts[0]
        cart.count += count
        cart.save()
    else:
        # 购物车中还没有商品
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
        cart.save()

    # json返回购物车中商品的总数量
    result = CartInfo.objects.filter(user_id=uid).count()
    return JsonResponse({'count': result})

def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(id = cart_id)
        cart.count = int(count)
        cart.save()
        data = {'ok': 0}
    except Exception:
        data = {'ok': 1}

    return JsonResponse(data)
def delete(request, cart_id):
    try:
        cart = CartInfo.objects.filter(id = cart_id)
        cart.delete()
        data = {'ok': 0}
    except:
        data = {'ok': 1}

    return JsonResponse(data)



