import ciphy
import os
import time
import pyautogui as auto


while True:
    auto.move(300, 0, duration=.75)
    auto.move(0, 300, duration=.75)
    auto.move(-300, 0, duration=.75)
    auto.move(0, -300, duration=.75)
    time.sleep(10)
