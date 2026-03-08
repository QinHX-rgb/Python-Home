from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from df_user.models import UserInfo
from df_cart.models import CartInfo
from df_order.models import OrderInfo, OrderDetailInfo
from df_goods.models import GoodsInfo
from datetime import datetime
from decimal import Decimal
from django.db import transaction


# Create your views here.
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
def order(request):
    # 获取用户信息
    uid = request.session.get('user_id')
    user = UserInfo.objects.get(id=uid)
    uphone = user.uphone[:3] + '****' + user.uphone[-4:]
    # 获取购物车中勾选的每个商品 构成列表 作为上下文参数传入到订单页面
    orderid = request.GET.getlist('orderid')
    orderlist = []
    for id in orderid:
        orderlist.append(CartInfo.objects.get(id=id))

    context = {'title': '提交订单',
               'user_center': 1,
               'user': user,
               'uphone': uphone,
               'orderlist': orderlist
    }
    return render(request, 'df_order/place_order.html', context)

@transaction.atomic()
@islogin
def addorder(request):
    '''返回Json数据 返回status=1表示成功 返回status=2表示失败 '''
    post = request.POST
    orderlist = post.getlist('ids[]')
    total = post.get('total')
    address = post.get('address')

    tran_id = transaction.savepoint()

    try:
        order = OrderInfo()
        now = datetime.now()
        uid = request.session.get('user_id')
        order.oid = '%s%d' % (now.strftime("%Y%m%d%H%M%S"), uid)  # 订单编号 通过时间戳和用户id生成 确保唯一性
        order.user_id = uid # 下订单的人
        order.odate = now # 下订单的日期
        order.oIsPay = False # 是否已经支付 默认未支付
        order.ototal = Decimal(total) # 总金额
        order.oaddress = address # 邮寄地址
        order.save()
        # 遍历购物车中提交信息 创建订单详情表
        for orderid in orderlist:
            cartinfo = CartInfo.objects.get(id=orderid)
            goodsinfo = GoodsInfo.objects.get(cartinfo__id=orderid)
        # 判断库存是否足够
            if int(goodsinfo.gkucun) >= int(cartinfo.count):
                # 库存足够 移除购买的数量
                goodsinfo.gkucun -= int(cartinfo.count)
                goodsinfo.save(update_fields=['gkucun'])

        # 创建订单详情表
                detailInfo = OrderDetailInfo()
                detailInfo.order_id = int(order.oid)
        #         # 订单
                detailInfo.goods_id = int(goodsinfo.id)
        #         # 对应的商品
                detailInfo.price = goodsinfo.gprice
        #         # 价格
                detailInfo.count = int(cartinfo.count)
                detailInfo.save()
        #         # 删除购物车中的对象
                cartinfo.delete()
            else: # 库存不够
                transaction.savepoint_rollback(tran_id)
                return JsonResponse({'status': 2})
    except Exception as e:
            transaction.savepoint_rollback(tran_id)
            return JsonResponse({'status': 2})

    return JsonResponse({'status': 1})


@transaction.atomic()
def pay(request, oid):
    # 把订单设置成已经支付状态
    order = OrderInfo.objects.get(oid=oid)
    order.oIsPay = True
    order.save()
    context = {'order': order}
    return render(request, 'df_order/pay.html', context)