import pyautogui
import time

xOffset = 100

while True:
    pyautogui.moveRel(xOffset, 0, duration=1)
    print('Mouse moved')
    xOffset = -xOffset  # toggle between positive and negative values
    time.sleep(10)
