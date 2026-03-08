# 字符串

name = input('请输入你的名字：')    # 输入
print('你好',name)  # 输出

content = '秦一航'      #定义字符串
content.replace("秦","亲")      # 替换字符串中的某个元素
print(content.replace("秦","亲"))

"""
方法/属性 说明 示例
str.lower()     将字符串转换为小写 "HELLO".lower() 返回 "hello"
str.upper()     将字符串转换为大写 "hello".upper() 返回 "HELLO"
str.capitalize()将字符串的首字母大写 "hello".capitalize() 返回 "Hello"
str.title()     将每个单词的首字母大写 "hello world".title() 返回 "Hello World"
str.strip()     移除字符串首尾的空白字符 " hello ".strip() 返回 "hello"
str.lstrip()    移除字符串左侧的空白字符 " hello ".lstrip() 返回 "hello "
str.rstrip()    移除字符串右侧的空白字符 " hello ".rstrip() 返回 " hello"
str.find(sub)   查找子字符串，返回子字符串的最低索引 "hello".find("lo") 返回 3
str.rfind(sub)  从右侧开始查找子字符串，返回子字符串的最高索引 "hello".rfind("l") 返回 2
str.replace(old, new)   替换字符串中的子字符串 "hello".replace("l", "x") 返回"hexxo"
str.split(sep)          以指定分隔符分割字符串 "hello world".split() 返回["hello", "world"]
str.join(iterable)      将序列中的元素以指定的字符串连接生成一个新的字符串 " ".join(["hello", "world"]) 返回"hello world"
str.startswith(prefix)  检查字符串是否以指定前缀开始 "hello".startswith("he") 返回True
str.endswith(suffix)    检查字符串是否以指定后缀结束 "hello".endswith("lo") 返回 True
str.isalpha()   检查字符串是否只包含字母 "hello".isalpha() 返回 True
str.isdigit()   检查字符串是否只包含数字 "123".isdigit() 返回 True
str.isalnum()   检查字符串是否只包含字母和数字 "hello123".isalnum() 返回 True
str.islower()   检查字符串是否全部为小写 "hello".islower() 返回 True
str.isupper()   检查字符串是否全部为大写 "HELLO".isupper() 返回 True
str.istitle()   检查字符串是否符合标题格式 "Hello World".istitle() 返回 True
str.len()       获取字符串长度 len("hello") 返回 5
str.count(sub)  计算子字符串出现的次数 "hello".count("l") 返回 2
str.format(*args,**kwargs)  格式化字符串 "{} is {}".format("hello","world") 返回 "hello is world"
"""