import time
from PIL import Image, ImageGrab
import keyboard
from mss import mss
from io import BytesIO
from pathlib import Path
import os
id = 0
ss_manager = mss()

frame = {"top":100, "left":300, "width":800, "height":165}

def take_screenshot(id):
    img = ss_manager.grab(frame)
    image = Image.frombytes("RGB", img.size, img.rgb)
    image.save("dataset/{}.png".format(id))

def move_id(id,key):
    os.system("mv dataset/{}.png dataset/{}/{}.png".format(id,key,id))
c
if __name__ == '__main__':
    time.sleep(10)
    while True:
        id += 1
        if is_exit:
            break

        take_screenshot(id)
        keys_pressed = [keyboard.is_pressed(key) for key in [keyboard.KEY_UP]]

        if not any(keys_pressed):
            move_id(id, "none")
            time.sleep(0.01)
            continue
        
        if keys_pressed[0]:
            move_id(id, "up")
            time.sleep(0.50)
