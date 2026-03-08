from DrissionPage import Chromium
import json

brother = Chromium()
with open("cookies.json","r",encoding = "utf-8") as f:
    cookies = json.load(f)

# cookies更新到浏览器中
brother.set.cookies(cookies)
tab = brother.get_tab()   #获取标签页
tab.get("https://uland.taobao.com/sem/tbsearch")  #打开淘宝首页
tab.wait(3)  #等待页面加载