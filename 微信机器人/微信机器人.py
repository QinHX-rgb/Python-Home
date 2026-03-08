import pyautogui as pg
import pyperclip as pc
import time
import random
from paddleocr import PaddleOCR

msg_strs = [
    "你好，有什么可以帮您的吗？",
    "您好，请问有什么需要帮助的？",
    "您好！很高兴为您服务，有什么可以帮您的吗？",
    "您好！请问有什么我可以帮您解答的？",
    "您好！需要帮助请随时告诉我。",
]

msg_dict = {
    "你好": "你好！很高兴认识你！",
    "吃了吗": "我是一名机器人，不需要吃饭哦！",
    "你是谁": "我是一个微信机器人，专门用来自动回复消息的。",
    "你会做什么": "我可以自动回复消息，帮你节省时间。",
    "滚": "好的，再见！",
    "在吗": "我一直在呢！有什么可以帮您的吗？"
}

def check_new_message():
    try:
        msg_center = pg.locateCenterOnScreen("E:\\desk\\Study Resources\\PythonProject\\project\\WX-robot\\new_msg.png")
        pg.click(msg_center)
        return True
    except:
        return False

def get_ocr_text(img_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    result = ocr.ocr(img_path)
    rec_texts = result[0]['rec_texts']
    ocr_txt = ''.join(rec_texts)
    return ocr_txt

def get_msg():
    pg.screenshot("msg.png",(341,750,532,58))
    ocr_txt = get_ocr_text("msg.png")
    return ocr_txt

def set_txt(msg):
    if msg in msg_dict:
        answer = msg_dict[msg]
    else:
        answer = random.choice(msg_strs)
    pc.copy(answer)
    pg.hotkey("ctrl", "v")

def return_home():
    try:
        file_center = pg.locateCenterOnScreen("E:\\desk\\Study Resources\\PythonProject\\project\\WX-robot\\home.png")
        pg.click(file_center)
    except:
        print("没找到文件传输助手图标")

while True:
    status = check_new_message()
    if status:
        msg = get_msg()
        set_txt(msg)
        pg.press("enter")
        return_home()
    time.sleep(1)

