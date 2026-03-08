from DrissionPage import Chromium
import time

brother = Chromium()
tab = brother.get_tab()   #获取标签页
tab.get("https://uland.taobao.com/sem/tbsearch")  #打开淘宝首页
time.sleep(180)
# 获取浏览器中的cookies

cookies = brother.cookies().as_json()
with open("cookies.json","w",encoding = "utf-8") as f:
    f.write(cookies)