#集合

#集合的创建
a_set = {10,20,30,40}
b_set = {'name',18,3.14,(10,20)}        #使用{}创建

s1 = set()          #创建一个空集合
s2 = set('Python')          #使用set()函数创建
print (s2)          #无序随机输出

#集合的常见操作
s = {1,2,3,4}
s.add(5)            #添加一个元素
print(s)
s.update({5,6,7})       #与新集合取并集
print(s)
s.discard(5)            #删除元素，如果元素不存在不会报错
print(s)
s.remove(6)             #删除元素，如果元素不存在会报错
print(s)
s.pop()             #随机删除一个元素
print (s)

#内置函数同样使用集合
print(len(a_set))       #求元素个数
print(max(a_set))       #求集合最大值
print(min(a_set))       #求集合最小值
print(sum(a_set))       #求和

#集合的运算
s1 = {1,5,7}
s2 = {5,10,15}

print(s1&s2)        #交集
print(s1|s2)        #并集   
print(s1-s2)        #差集
print(s1^s2)        #补集
print(s1<=s2)       #s1是s2的补集返回True，否则返回False
print(s1>=s2)       #s1是s2的超集返回True，否则返回False