import cv2
import numpy as np
import os
import csv
import tkinter
import main
from tkinter.filedialog import asksaveasfile

listPoints = []
img = np.zeros((640,480,3), np.uint8)

def drawCircle(event, x, y, flags, param):
    global listPoints

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
        listPoints.append([x, y])

def saveCSV(savefile):
    print('Salvando arquivos')
    # Escreve o arquivo csv
    with open(savefile.name, mode='w') as csv_file:
        header = ['num. bola', 'x', 'y', 'auto']

        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()

        for i in range(0, len(listPoints)):
            writer.writerow(
                {'num. bola': i + 1, 'x': listPoints[i][0], 'y': listPoints[i][1], 'auto': 1})

def calibcam(filename):

    global img
    global listPoints

    titleWindow = "ESC - Sair; M - Mostrar coordenadas; R - Resetar coordenadas; S - Salvar coordenadas e sair"
    
    img = cv2.imread(filename)
    cv2.namedWindow(titleWindow)
    cv2.setMouseCallback(titleWindow, drawCircle)

    exit = False
    save = False

    for i in range(0, len(listPoints)):
        cv2.circle(img, (listPoints[i][0], listPoints[i][1]), 10, (255, 0, 0), -1)

    while(not exit):
        cv2.imshow(titleWindow, img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == ord('m'):
            for i in range(0, len(listPoints)):
                print(listPoints[i])
        elif k == ord('r'):
            listPoints = []
            img = cv2.imread(filename)
        elif k == ord('s'):
            save = True
            exit = True
            
    cv2.destroyAllWindows()

    if (save):
        window = tkinter.Tk()
        # asksaveasfile return `None` if dialog closed with "cancel".
        savefile = asksaveasfile(mode='w', defaultextension=".csv")
        window.destroy()
        if savefile is None: 
            calibcam(filename)
        else:
            saveCSV(savefile)
            main.main()
    else:
        main.main()
