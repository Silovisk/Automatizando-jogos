import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Retorna x e y e RGB
#X: 3918 Y:  240 RGB: (NaN, NaN, NaN)
#pyautogui.displayMousePosition()

#https://lagged.com.br/pt/g/piano-tiles

'''
1 linha
diferença 161 em x 
X:  568 Y:  270 RGB: ( 35,  35,  41)
X:  729 Y:  270 RGB: (101, 101, 101)
X:  900 Y:  270 RGB: (101, 101, 101)
X: 1061 Y:  270 RGB: ( 35,  35,  41)

2 linha
Diferenca 184 em y 
X:  545 Y:  454 RGB: ( 35,  35,  41)
X:  736 Y:  454 RGB: (211, 211, 211)
'''

def clicar(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


matriz = [
     [(568, 270), (729, 270), (890, 270), (1051, 270)],
     [(568, 454), (729, 454), (890, 454), (1051, 454)],
     [(568, 638), (729, 638), (890, 638), (1051, 638)],
     [(568, 822), (729, 822), (890, 822), (1051, 822)]
]

'''
# Funcao para retornar a matriz correta das posicoes da imagem piano_tiles_reflex.png

matriz = []

for i in range(4):
    linha = []
    x = 568
    y = 270 + i * 184

    for j in range(4):
        linha.append((x, y))
        x += 161

    matriz.append(linha)
for linha in matriz:
    print(linha)

'''

while not keyboard.is_pressed('z'):
     for linha in matriz:
          for posicao in linha:
               pixel = pyautogui.pixel(posicao[0], posicao[1])
               if pixel[0] != 211:
                    clicar(posicao[0], posicao[1])
