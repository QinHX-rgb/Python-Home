#元组（元素不能改变）

#使用（）创建元组
a = ()      #创建一个空元组
b = 1,      #由逗号结尾表示元组
c = (1,)        #单个元素的元组
d = (1,2,3)         #包含多个元素的元组

print (a)
print (b)
print (c)
print (d)

#使用tuple（）创建元组，或将字符串、列表等转换为元组
a = tuple([1,2,3,4])        #定义元组a
print(a)

#元组应用场景
x,y = 10,20         #多变量同步赋值
print (x,y)

for x in ((10,20),(15,25)):         #循环遍历
    print(x)
for x,y in ((10,20),(15,25)):       #循环遍历
    print(x,y)

"""
count(x)    返回元素 x 在元组中出现的次数。 tup = (1, 2, 3,2, 4) tup.count(2) 输出：2
index(x)    返回元素 x 在元组中第一次出现的位置（索引）。如果不存在，抛出 ValueError。tup = (1, 2, 3,2, 4) tup.index(2) 输出：1
len(tup)    返回元组中的元素个数。tup = (1, 2, 3,2, 4) len(tup)  输出：5
tup + tup2  将两个元组合并成一个新元组。tup1 = (1, 2, 3) tup2 = (4, 5) tup1 + tup2 输出：(1, 2, 3, 4, 5)
tup * n     将元组中的元素重复 n 次，返回新元组。tup = (1, 2)tup * 3  输出：(1,2, 1, 2, 1, 2)
tuple(iter) 将一个可迭代对象转换成元组。list = [1, 2, 3] tuple(list)  输出：(1, 2, 3)
min(tup)    返回元组中最小的元素。tup = (5, 1, 9,3, 7) min(tup)  输出：1
max(tup)    返回元组中最大的元素。tup = (5, 1, 9,3, 7)max(tup)  输出：9
sorted(tup) 返回一个新列表，包含元组中的元素，按照升序排序。tup = (5, 1, 9,3, 7)sorted(tup)  输出：[1, 3, 5, 7, 9]
tup[索引]   访问元组中指定索引位置的元素。tup = (1, 2, 3,4, 5)tup[2]  输出：3
tup[start:stop:step]    切片操作，返回元组中从 start 到 stop（不包含stop）的元素，步长为 step。tup = (1, 2, 3,4, 5)tup[1:4:2]  输出：(2, 4)
"""