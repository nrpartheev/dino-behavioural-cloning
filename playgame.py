import time
from PIL import Image
from mss import mss
import keyboard
import numpy as np
from keras.models import model_from_json


frame = {"top":100, "left":300, "width":800, "height":165}
ss_manager = mss()  
is_exit = False    
my_timer = 0        
width = 800     
height = 165   


def up():
    keyboard.release("right")
    keyboard.release(keyboard.KEY_DOWN)
    keyboard.press(keyboard.KEY_UP)


if __name__ == '__main__':
    keyboard.add_hotkey("esc", exit)  
    model = model_from_json(open("model.json","r").read())
    model.load_weights("weights.h5")

    while True:
        screenshot = ss_manager.grab(frame)
        image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        grey_image = image.convert("L")                       
        a_img = np.array(grey_image.resize((width, height)))  
        img = a_img / 255                                     
        X = np.array([img])                                 
        X = X.reshape(X.shape[0], width, height, 1)         
        prediction = model.predict(X)                       
        result = np.argmax(prediction) 
        if result == 2: 
            time.sleep(0.1)
            up()
        
