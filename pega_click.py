import cv2
import numpy as np
import os
import csv

# mouse callback function

# lista_pontos[posicao][x][y];
lista_pontos = []
cont = 0

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
        lista_pontos.append([x, y])

def salvar_csv():
    print('Salvando arquivos')
    # Escreve o arquivo csv
    with open(os.getcwd() + '/csv_click/' + 'camera_3' + '.csv', mode='w') as csv_file:
        header = ['num. bola', 'x', 'y']

        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()

        for i in range(0, len(lista_pontos)):
            writer.writerow(
                {'num. bola': i + 1, 'x': lista_pontos[i][0], 'y': lista_pontos[i][1]})


    # Create a black image, a window and bind the function to window
img = cv2.imread("blender/camera_3 (copy).png")
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('m'):
        for i in range(0, len(lista_pontos)):
            print(lista_pontos[i])
    elif k == ord('r'):
        lista_pontos = []
        img = cv2.imread("blender/camera_3 (copy).png")
        cont = 0
    elif k == ord('s'):
        salvar_csv()

cv2.destroyAllWindows()

# https://stackoverflow.com/questions/50005058/image-browser-using-python

