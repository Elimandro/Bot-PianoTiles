#INSTALAR LO SIGUIENTE A TRAVES DE LA CONSOLA:
#pip install pywin32
#pip install keyboard
#pip install pyautogui
#pip install opencv-python
#pip install Pillow

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#USAR LOS SIGUIENTES COMANDOS EN IDLE SHELL __ (TU VERSION DE PYTHON 🐍) PARA SABER LA POSICION
#DEL PIXEL QUE DESEAS TOCAR Y MANEJAR:

#import pyautogui
#pyautogui.displayMousePosition()

#POSICION DE LOS PIXLES A FIJAR (EN MI CASO):
#                            POSICION EN X y Y
#                                ↓       ↓
#POSICION DE LOS PIXLES Position X:  363 Y:  400 RGB: (0, 0, 0)  ← COLOR DEL PIXEL
#POSICION DE LOS PIXLES Position X:  438 Y:  400 RGB: (0, 0, 0)
#POSICION DE LOS PIXELES Position X:  514 Y:  400 RGB: (0, 0, 0)
#POSICION DE LOS PIXELES Position X:  590 Y:  400 RGB: (0, 0, 0)

#SE OCUPA "Y: 400" PARA UNIFICAR LA POSICION DEL MOUSE SOBRE LOS PIXELES, SIMPLIFICANDO EL PROCESO BASTENTE...

def click(x,y): # ← FUNCION PARA COORDENADAS, CLICK Y DELAY...
    win32api.SetCursorPos((x,y))  
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) # ← PAUSA EL SCRIPT DEL BOT POR 0.1 SEGUNDOS
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed("q") == False: # ← TECLA PARA FINALIZAR ES "Q" PUEDES USAR LA QUE TE GUSTE

    if pyautogui.pixel(363, 400)[0] == 0: # ← PRIMERA COLUMNA COORDENADAS, CONFIRMACION DEL COLOR Y CLICK EN LA COORDENADA
        click(363, 400)
    if pyautogui.pixel(438, 400)[0] == 0: # ← SEGUNDA COLUMNA COORDENADAS, CONFIRMACION DEL COLOR Y CLICK EN LA COORDENADA
        click(438, 400)
    if pyautogui.pixel(514, 400)[0] == 0: # ← TERCERA COLUMNA COORDENADAS, CONFIRMACION DEL COLOR Y CLICK EN LA COORDENADA
        click(514, 400)
    if pyautogui.pixel(590, 400)[0] == 0: # ← CUARTA COLUMNA COORDENADAS, CONFIRMACION DEL COLOR Y CLICK EN LA COORDENADA
        click(590, 400)    

#CABE ACLARAR ESTOY INICIANDO CON PYTHON 🐍 Y MIRE UN TUTORIAL PARA HACERLO
#HARE UN EJECUTABLE CON UI MAS DELANTE PARA ESTE MINI BOT/SCRIPT... 🧑🏻‍💻
#GRACIAS POR VER, QUE DIOS TE BENDIGA Y RECUERDA EL NOS AMA... ✝️
