from django.shortcuts import render

from df_cart.models import CartInfo
from df_goods.models import *
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    if request.session.get('user_id'):
        uid = request.session.get('user_id')
        result = CartInfo.objects.filter(user_id=uid).count()
    else:
        result = 0
    fruit = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[:4]  # 最新产品
    fruit2 = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[:3]  # 热销产品
    fish = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[:4]  # 最新产品
    fish2 = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[:3]  # 热销产品
    meat = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[:4]  # 最新产品
    meat2 = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[:3]  # 热销产品
    egg = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[:4]  # 最新产品
    egg2 = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[:3]  # 热销产品
    vegetable = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[:4]  # 最新产品
    vegetable2 = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[:3]  # 热销产品
    frozen = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[:4]  # 最新产品
    frozen2 = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[:3]  # 热销产品

    context = {'title': '天天书城-首页',
               'fruit': fruit, 'fruit2': fruit2,
               'fish': fish, 'fish2': fish2,
               'meat': meat, 'meat2': meat2,
               'egg': egg, 'egg2': egg2,
               'vegetable': vegetable, 'vegetable2': vegetable2,
               'frozen': frozen, 'frozen2': frozen2,
               'result': result
               }
    return render(request, 'df_goods/index.html', context)


def list(request, typeid, pageid, sort):
    if request.session.get('user_id'):
        uid = request.session.get('user_id')
        result = CartInfo.objects.filter(user_id=uid).count()
    else:
        result = 0

    type = TypeInfo.objects.get(id=typeid)
    newgoods = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')[:2]  # 新品推荐

    # 获取所有的商品 并按默认（新品）排序
    if sort == '1':
        newgoodslist = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')
    elif sort == '2':
        newgoodslist = GoodsInfo.objects.filter(gtype_id=typeid).order_by('gprice')
    elif sort == '3':
        newgoodslist = GoodsInfo.objects.filter(gtype_id=typeid).order_by('gclick')

    # 分页
    paginator = Paginator(newgoodslist, 4)
    goodlist = paginator.page(int(pageid))

    pindexlist = paginator.page_range  # 所有页的id

    context = {'title': '天天书城-商品列表',
               'newgoods': newgoods,
               'type': type,
               'goodlist': goodlist,
               'typeid': typeid, 'sort': sort,
               'pindexlist': pindexlist, 'pageid': int(pageid),
               'result': result, }
    return render(request, 'df_goods/list.html', context)


def detail(request, id):
    if request.session.get('user_id'):
        uid = request.session.get('user_id')
        result = CartInfo.objects.filter(user_id=uid).count()
    else:
        result = 0
    # 获取产品类型id
    typeid = GoodsInfo.objects.get(id=id).gtype_id
    # 获取产品类型
    goodType = TypeInfo.objects.get(id=typeid)
    # 获取最新发布的产品（2个）
    newgood = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')[:2]

    # 获取当前商品的对象
    goods = GoodsInfo.objects.get(id=id)
    # 增加访问量 点击量
    goods.gclick += 1
    goods.save()

    context = {'title': '天天书城-商品详情',
               'guest_cart': 1,
               'newgood': newgood,
               'typeid': typeid,
               'goodType': goodType,
               'goods': goods,
               'result': result, }

    response = render(request, 'df_goods/detail.html', context)
    # 读取请求的cookie
    goods_ids = request.COOKIES.get('goods_ids')  # 5,2,7
    # 判断cookie中的商品id序列是否为空
    if goods_ids and goods_ids != '':
        # 不为空 以逗号分隔 把字符串转换为列表
        goods_ids = goods_ids.split(',')
        # 如果列表中已经有当前id 则需要删除列表中原来的id
        if id in goods_ids:
            goods_ids.remove(id)
        # 把当前的id插入到列表的最前面
        goods_ids.insert(0, id)
        # 取前5个
        if len(goods_ids) > 5:
            goods_ids = goods_ids[:5]
    else:
        # 为空
        goods_ids = id

    # print(type(goods_ids))
    # 转字符串 [9,5,2,7] --- "9,5,2,7"
    # 使用逗号来连接列表中的每一个元素
    goods_ids = ','.join(goods_ids)
    # 添加cookie信息
    response.set_cookie('goods_ids', goods_ids)

