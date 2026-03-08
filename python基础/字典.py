#字典

#字典的创建
a_dict = {'name':'小明','age':18}
b_dict = {'a':1,'b':2,'c':3}            #使用{}创建字典

c_dict = dict(name = '小明',age=18)     #使用dict()函数创建字典

#字典元素的读取
print (a_dict['name'])          #通过'name'键访问'小明'（下标法）
#printf(a_dict['tel'])          指定的键不存在，返回异常

print (a_dict.get('name'))      #通过get（）访问'小明'（get()法）
print (a_dict.get('tel'))       #指定的键不存在，返回None

for key,value in a_dict.items():
    print (key,value)           #通过for循环遍历子弟啊的键和值（items()法）

#字典元素的添加
a_dict = {'name':'小明','age':18}

a_dict['tel']='123456'          
print (a_dict['tel'])           #直接添加

a_dict.update(b_dict)
print (a_dict)              #通过update()函数添加字典

#字典元素的修改
a_dict['name'] = '小丽'
print(a_dict)               #直接修改字典元素

#字典元素的删除
del a_dict['age']           #删除指定键
print(a_dict)

a_dict.pop('name')          #删除指定键
print(a_dict)

a_dict.popitem()            #删除随机键
print(a_dict)