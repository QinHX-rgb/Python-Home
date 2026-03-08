from DrissionPage import Chromium
import json

brother = Chromium()
with open("cookies.json","r",encoding = "utf-8") as f:
    cookies = json.load(f)

print(cookies)
# cookies更新到浏览器中
brother.set.cookies(cookies)
tab = brother.get_tab()   #获取标签页
tab.get("https://www.toutiao.com")  #打开今日头条首页
tab.wait(3)  #等待页面加载