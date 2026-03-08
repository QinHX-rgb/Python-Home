import random

class Pikaqiu():
    def __init__(self,name):
        self.blood = random.randint(150,200)
        self.name = name

    def show(self):
        print(f"我的名字是：{self.name},我的血量为{self.blood}" )

    def shiwanfute(self,victim):
        victim.blood -= 50
        skill_name = "十万伏特"
        print(f"{self.name}使用{skill_name}攻击了{victim.name},{victim.name}剩余血量为：{victim.blood}")

    def niepan(self):
        self.blood += 99
        skill_name = "涅槃"
        print(f"{self.name}使用{skill_name}，血量增加为为：{self.blood}")

    def shangcangzhishou(self,victim):
        victim.blood -= 100
        skill_name = "上苍之手"
        print(f"{self.name}使用{skill_name}攻击了{victim.name},{victim.name}剩余血量为：{victim.blood}")
  

p1 = Pikaqiu("皮卡丘1号")
p1.show()
print()

p1.niepan()