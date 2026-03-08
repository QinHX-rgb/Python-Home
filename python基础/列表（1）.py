#列表创建与访问

#直接用方括号定义列表
names = ['张三','李四','王五','赵六']
print(names[1])     #使用索引进行访问

#使用list()函数定义列表
li_two = list ('python')        #字符串转化为列表
li_three = list ((1,'python'))      #元组转化为列表

#使用索引访问列表
print (li_two[3])       #使用索引进行访问
print (li_three[1])         #使用索引进行访问

#使用切片法访问列表
li_four = li_three[:3]      #切片法不改变原列表
print (li_two[2:])      #使用切片方式访问索引为2~末尾的元素
print (li_three[:3])        #使用切片方式访问索引为0~3的元素
print (li_two[:])       #使用切片法获取所有元素

#for 循环因子 in 列表：
#    语句块（缩进）
for name in names:
    print(name)

