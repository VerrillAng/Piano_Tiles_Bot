from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con


# Tile 1 - 900, 845
# Tile 2 - 1030, 845
# Tile 3 - 1160, 845
# Tile 4 - 1290, 845

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main():
    while True:
        if keyboard.is_pressed('s'):
            while not keyboard.is_pressed('q'):
                if pyautogui.pixel(900, 845)[0] == 0:
                    click(900, 845)

                if pyautogui.pixel(1030, 845)[0] == 0:
                    click(1030, 845)

                if pyautogui.pixel(1160, 845)[0] == 0:
                    click(1160, 845)

                if pyautogui.pixel(1290, 845)[0] == 0:
                    click(1290, 845)

                if keyboard.is_pressed('q'):
                    exit(0)


if __name__ == '__main__':
    main()
