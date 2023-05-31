import pyautogui
import time

xOffset = 100

for i in range(10):
    pyautogui.moveRel(xOffset, 0, duration=1)
    xOffset = -xOffset  # toggle between positive and negative values
    time.sleep(10)
