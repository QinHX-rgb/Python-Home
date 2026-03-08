#操作列表

#列表元素的添加
list_1 = [1,2,3,4]
list_2 = ['a','b','c','d']
list_1.append(5)        #在末尾添加元素
print (list_1)
list_1.extend(list_2)       #在末尾添加列表/字符串
print (list_1)          
list_1.insert(5,'Hello')        #在list_1索引为5的位置添加字符串'Hello'
print (list_1)

#列表元素的删除
list_3 = [1,2,3,4,5,1,2,3]

list_3.remove(2)        #移除指定元素2，但只会移除第一个
print (list_3)
list_3.pop(2)           #移除下标为2的元素
print (list_3)
list_3.pop()        #不指明删除哪一个，默认最后一个
print(list_3)
del list_3[1]       #删除下标为1的元素,不指明就全部删除
print(list_3)

#列表元素的修改
list_4 = ['python','java','C']

list_4[2] = 'C++'       #将索引为2的元素C修改为C++
print (list_4[2])

#列表元素的排序
x = [2,5,7,3,9,10,5,7]

#sort方法
x.sort(reverse=False)        #False一般不用写，默认升序排列
print (x)
x.sort(reverse=True)        #Ture为降序排列
print(x)
x.sort(key=str)     #按字符串升序排列
print(x)

#reverse()方法
y = ['a','b','c','d']
y.reverse()        #将列表元素从右至左倒序排列
print(y)

#列表元素个数
n = len(x)
print(n)


"""
append(x)   在列表末尾添加一个元素 x lst.append(1)
extend(iterable)    将一个可迭代对象（如另一个列表）的所有元素添加到列表末尾 lst.extend([2, 3])
insert(i, x)    在指定位置 i 插入一个元素 x lst.insert(0, 0)
remove(x)   移除列表中第一个值为 x 的元素 lst.remove(1)
pop([i])    移除列表中指定位置 i 的元素，并返回该元素。如果不指定位置，默认移除并返回列表中的最后一个元素 lst.pop() 或 lst.pop(0)
clear()     清空列表中的所有元素 lst.clear()index(x[,
start[, end]])  返回列表中第一个值为 x 的元素的索引，可以指定搜索的起始和结束位置 lst.index(2)或lst.index(2, 1, 5)
count(x)    返回 x 在列表中出现的次数 lst.count(2)
sort(key=None,reverse=False)    对列表中的元素进行排序 lst.sort()或lst.sort(reverse=True)
reverse()   反转列表中的元素顺序 lst.reverse()
copy()      返回列表的浅拷贝 new_lst = lst.copy()
len(lst)    返回列表长度 length = len(lst)
min(lst)    返回列表中的最小值 min_value = min(lst)
max(lst)    返回列表中的最大值 max_value = max(lst)
sum(lst)    返回列表中所有元素的和 total = sum(lst)
"""