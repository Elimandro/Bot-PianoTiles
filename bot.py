from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#posicion de las teclas Position X:  363 Y:  400 RGB: (0,  0,   0)
#posicion de las teclas Position X:  438 Y:  400 RGB: (155, 161, 230)
#posicion de las teclas Position X:  514 Y:  400 RGB: (153, 159, 230)
#posicion de las teclas Position X:  590 Y:  400 RGB: (168, 172, 232)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #pausa el script 0.01 segundo
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(363, 400)[0] == 0:
        click(363, 400)
    if pyautogui.pixel(438, 400)[0] == 0:
        click(438, 400)
    if pyautogui.pixel(514, 400)[0] == 0:
        click(514, 400)
    if pyautogui.pixel(590, 400)[0] == 0:
        click(590, 400)    
