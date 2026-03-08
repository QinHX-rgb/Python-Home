from pynput.mouse import Button, Controller as mouse_Controller
from pynput.keyboard import Key, Controller as key_Controller
import time
import random

f = open('轰炸.txt', encoding='utf-8')
txt = f.read()
lis_text = txt.split('\n')
time.sleep(3)

mouse = mouse_Controller()  # 控制鼠标
keyboard = key_Controller()
mouse.press(Button.left)  # 按住鼠标左键
mouse.release(Button.left)  # 松开鼠标左键
for i in range(99):
    key_world = random.choice(lis_text)
    time.sleep(0.5)
    keyboard.type(key_world)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)