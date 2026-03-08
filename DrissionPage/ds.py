from DrissionPage import Chromium


brother = Chromium()
tab = brother.get_tab()   #获取标签页
tab.get("https://www.baidu.com")  #打开百度首页

# # 精准获取
# . == @class=
# eles = tab.eles(".hotsearch-item odd")
# # print(eles)
# for ele in eles:
#     print(ele.text)

# eles = tab.eles("@class=hotsearch-item even")
# # print(eles)
# for ele in eles:
#     print(ele.text)

# 模糊获取
# eles = tab.eles("@class:hotsearch-item")  #获取所有热搜项
# for ele in eles:
#     print(ele.text)

# # 基于父标签
# father_ele = tab.ele(".s-hotsearch-content")
# # 获取所有的li标签 @tag
# eles = father_ele.eles("@tag()=li")
# for ele in eles:
#     print(ele.text)

# 通过ID定位
# father_ele = tab.ele("@id=hotsearch-content-wrapper")
# eles = father_ele.eles("@tag()=li")
# for ele in eles:    
#     print(ele.text)

# # 获取输入框
# input_ele = tab.ele("#chat-textarea")
# # 清除输入框内容
# input_ele.clear()
# # 输入内容
# input_ele.input("怀轩")
# # tab.ele("#chat-submit-button").click()  #点击搜索按钮
# tab.ele("@text()= 百度一下 ").click()

# keywords = ["python","DrissionPage","自动化测试"]
# for keyword in keywords:
#     input_ele = tab.ele("#chat-textarea")
#     input_ele.clear()
#     input_ele.input(keyword)
#     tab.ele("@id=chat-submit-button").click()
#     tab.wait(4) # 等待页面加载
#     tab.scroll.to_bottom()  # 滚动到页面底部，加载全部内容
#     tab.wait(2)
#     content_left = tab.ele("#content_left")
#     content_left_text = content_left.text   
#     with open(f"{keyword}.txt","w",encoding="utf-8") as f:  
#         f.write(content_left_text)  


# 全屏截图
tab.get_screenshot("all.png")

# 元素截图
lg = tab.ele("#lg")
lg.get_screenshot("lg.png")