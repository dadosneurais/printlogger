import pyautogui
import datetime
import time

interval = 10*60 #a cada 10 minutos um print
fileDir = "local_arquivo/_"
fileName = "print"

while True:
    #obter o tempo atual
    timeStamp = datetime.datetime.now().strftime("%Hh%Mm") # se quiser add segundos é %Ss

    #obter a data atual
    date = datetime.datetime.now().strftime("%d-%m-%y")

    #gera o nome do arquivo
    printImg = f"{fileDir}{fileName}_{timeStamp}_{date}.png"

    #sava a img
    img = pyautogui.screenshot()
    img.save(printImg)

    #aguarda o intervalo para os próximos prints
    time.sleep(interval)
