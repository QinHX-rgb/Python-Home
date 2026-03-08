import random

class Pikaqiu():
    def __init__(self,name):
        self.blood = random.randint(200,300)
        self.name = name

    def show(self):
        print(f"我的名字是：{self.name},我的基础血量为{self.blood}" )

    def shiwanfute(self,victim):
        victim.blood -= 88
        skill_name = "十万伏特"
        print(f"{self.name} 使用 {skill_name} 攻击了 {victim.name} , {victim.name} 剩余血量为：{victim.blood}")

    def niepan(self):
        self.blood += 99
        skill_name = "涅槃"
        print(f"{self.name} 使用 {skill_name}，血量增加为：{self.blood}")

    def shangcangzhishou(self,victim):
        victim.blood -= 100
        skill_name = "上苍之手"
        print(f"{self.name} 使用 {skill_name} 攻击了 {victim.name} , {victim.name} 剩余血量为：{victim.blood}")


class SPikaqiu(Pikaqiu):
    color = "彩色"

    def leitingwanjun(self,victim):
        victim.blood -= 66
        skill_name = "雷霆万钧（变异专属技能）"
        print(f"{self.name} 使用 {skill_name} 攻击了 {victim.name} , {victim.name} 剩余血量为：{victim.blood}")
  

class Xiaohuolong():
    color = "红色"
    def __init__(self,name):
        self.blood = random.randint(150,200)
        self.name = name

    def show(self):
        print(f"我的名字是：{self.name},我的基础血量为{self.blood}" )

    def chiwoyijiba(self,victim):
        victim.blood -= 99
        skill_name = "吃我一戟吧"
        print(f"{self.name} 使用 {skill_name} 攻击了 {victim.name} , {victim.name} 剩余血量为：{victim.blood}")


class Huoqiulong(Pikaqiu,Xiaohuolong):
    color = "橙色"
    def __init__(self,name):
        self.blood = random.randint(150,200)
        self.name = name
    def show(self):
        print(f"我的名字是：{self.name},我的基础血量为{self.blood}" )


p1 = Huoqiulong("郑杰丰")
p2 = SPikaqiu("张智杰")
p3 = Xiaohuolong("刘振赢")

p1.show()
p2.show()
p3.show()
print()

p1.shiwanfute(p2)
p1.shangcangzhishou(p3)
p2.leitingwanjun(p1)
p3.chiwoyijiba(p1)
p1.niepan()


