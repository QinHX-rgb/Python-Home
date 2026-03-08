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

tab.ele("#q").input("工装裤")
tab.ele("#button").click()  # 搜索商品
tab.wait(3)  # 等待页面加载

shop_card_eles = tab.eles("@class:CardV2--doubleCardWrapper--rq81FGu")
infos = []

for i in range(3):
    print(f"正在爬取第{i+1}页----")

    tab.scroll.to_top()
    for page in range(15):
        tab.scroll(300)
        tab.wait(0.5)

    for shop_card_ele in shop_card_eles:
        info = {}

        title = shop_card_ele.ele(".:Title--title--wJY8TeA")
        info["标题"] = title.text

        img = shop_card_ele.ele(".:MainPic--mainPicWrapper--varchHg")
        info["图片链接"] = img.ele("@tag()=img").attr("src")

        shop_name = shop_card_ele.ele(".=ShopInfo--shopNameText--kxQC2cC")
        info["店铺名称"] = shop_name.text

        priceInt = shop_card_ele.ele(".Price--priceInt--BXYeCOI").text
        priceFloat = shop_card_ele.ele(".Price--priceFloat--rI_BYho").text
        price = priceInt + priceFloat
        info["价格"] = price

        place = shop_card_ele.eles(".Price--procity--Na1DQVe")
        info["市"] = ""
        if len(place) > 1:
            info["市"] = place[1].text
        info["省/直辖市"] = place[0].text

        idx = len(infos) + 1
        wrapped = {f"第{idx}件商品": info}
        infos.append(wrapped)

        tab.ele(".=next-btn-helper").click() # 翻页



# 导出为 Excel
try:
    import pandas as pd
except ImportError:
    print("未找到 pandas，若需导出请先安装：pip install pandas openpyxl")
else:
    rows = []
    for wrapped in infos:
        for k, v in wrapped.items():
            row = v.copy()
            row["序号"] = k
            rows.append(row)

    if rows:
        df = pd.DataFrame(rows)
        cols = ["序号"] + [c for c in df.columns if c != "序号"]
        df = df[cols]
        df.to_excel("商品信息.xlsx", index=False)
        print("已保存到 商品信息.xlsx")
    else:
        print("infos 为空，未生成 Excel 文件")


