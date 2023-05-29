import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Retorna x e y e RGB
#X: 3918 Y:  240 RGB: (NaN, NaN, NaN)
#pyautogui.displayMousePosition()

# https://www.agame.com/game/magic-piano-tiles
'''
1 - X:  426 Y:  700 RGB: (169, 173, 232)
2 - X:  567 Y:  700 RGB: (189, 192, 236)
3 - X:  692 Y:  700 RGB: (  0,   0,   0)
4 - X:  830 Y:  700 RGB: (158, 164, 231)
'''

posicoes = [
     (426, 700),
     (567, 700),
     (692, 700),
     (830, 700)
]



def clicar(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('z'):
     for posicao in posicoes:
          pixel = pyautogui.pixel(posicao[0], posicao[1])
          if pixel[0] == 0:
               clicar(posicao[0], posicao[1])
               
"""
while keyboard.is_pressed('z') == False:
     if pyautogui.pixel(position_1[0], position_1[1])[0] == 0:
          clicar(position_1[0], position_1[1])

     if pyautogui.pixel(position_2[0], position_2[1])[0] == 0:
          clicar(position_2[0], position_2[1])

     if pyautogui.pixel(position_3[0], position_3[1])[0] == 0:
          clicar(position_3[0], position_3[1])

     if pyautogui.pixel(position_4[0], position_4[1])[0] == 0:
          clicar(position_4[0], position_4[1])
"""
