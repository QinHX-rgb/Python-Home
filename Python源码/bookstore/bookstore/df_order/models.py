Rfrom django.db import models

# Create your models here.
# 订单信息
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True)
    # 订单编号
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)
    # 下订单的人
    odate = models.DateTimeField(auto_now=True)
    # 下订单的日期
    oIsPay = models.BooleanField(default=False)
    # 是否已经支付 默认未支付
    ototal = models.DecimalField(max_digits=6, decimal_places=2)
    # 总金额
    oaddress = models.CharField(max_length=200)
    # 邮寄地址

    #  订单详情
class OrderDetailInfo(models.Model):
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    # 订单
    goods = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE)
    # 对应的商品
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # 价格
    count = models.IntegerField()
    # 数量