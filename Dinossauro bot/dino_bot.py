from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
from numpy import * 

TOT_CINZA = 3547

class Cordenadas(): 
    #Cordenada do botao reiniciar
    btn_reiniciar = (960, 586)

    #Cordenadas superiores direitas da cabeça do dino
    dinossauro = (611, 594)
    #x = 100 y=415 
    
#Reiniciar  o Jogo      
def ReinciarJogo(): 
    pyautogui.click(Cordenadas.btn_reiniciar)

#Pressionar  o Espaço  
def PressionarEspaco(): 
    pyautogui.keyDown('space')     
    time.sleep(0.05) 
    print('Jump') 
    pyautogui.keyUp('space') 

def imageGrab(): 
    box = (Cordenadas.dinossauro[0] + 60 ,Cordenadas.dinossauro[1], 
           Cordenadas. dinossauro[0] + 170 ,Cordenadas.dinossauro[1]+30)            
    
    #verifica  se existe uma 'Imagem' nossa coordenada 
    #coordDinoX , coordDinoY, CoordLimtyX, CoordLimityY 

    imagem = ImageGrab.grab(box) 
    imagem_cinza = ImageOps.grayscale(imagem) 
    a = array(imagem_cinza.getcolors())  

    if a.sum() != TOT_CINZA: 
        print(a.sum()) 
                
    return a.sum() 


def main(): 
    ReinciarJogo()   
    while True: 
        if(imageGrab()!= TOT_CINZA):  
            PressionarEspaco() 
            time.sleep(0.1)
        
  
main()     