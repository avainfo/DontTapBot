import math
import time

import win32api
import win32con
from PIL import ImageGrab
from pynput import mouse

SCREEN_X = 655
SCREEN_Y = 263
CELL_SIZE = 151
DELAY_BETWEEN_READS = 0.2


def click(x, y):
    win32api.SetCursorPos((SCREEN_X + x, SCREEN_Y + y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def read_screen():
    x = ImageGrab.grab(bbox=(SCREEN_X, SCREEN_Y, SCREEN_X + 1, SCREEN_Y + 1)).load()[0, 0]
    while str(x) == "(25, 25, 25)":
        x = ImageGrab.grab(bbox=(SCREEN_X, SCREEN_Y, SCREEN_X + 1, SCREEN_Y + 1)).load()[0, 0]
        time.sleep(DELAY_BETWEEN_READS)
    for i in range(1000):
        pic = ImageGrab.grab(bbox=(SCREEN_X - 12, SCREEN_Y - 12, SCREEN_X + 613 - 12, SCREEN_Y + 613 - 12)).load()
        d = {}
        index = 0
        for i in range(0, 4):
            for j in range(0, 4):
                d[index] = pic[75 + (CELL_SIZE * j), 75 + (CELL_SIZE * i)]
                index += 1
        for k, v in d.items():
            if v == (0, 0, 0):
                row = math.floor(k / 4)
                col = k - 4 * row
                click(75 + (CELL_SIZE * col), 75 + (CELL_SIZE * row))
                time.sleep(0.1)


def on_click(x, y, button, pressed):
    global started
    if button == mouse.Button.left and not started:
        time.sleep(1)
        started = True
        read_screen()


started = False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
