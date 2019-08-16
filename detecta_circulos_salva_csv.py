import os
import numpy as np
import argparse
import cv2
import csv

# Percorre todas as imagens, acha os circulos e depois escreve em csv
for file in os.listdir(os.getcwd() + '/imagens'):
    image = cv2.imread("imagens/" + file)
    output = image.copy()
    # Cnverte para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Função do opencv para detectar circulos
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.4, 100)

    # Verifica se foi encontrado algum circulo
    if circles is not None:
        # Converte (x, y) coordenadas and raio do circulo para inteiro
        circles = np.round(circles[0, :]).astype("int")

        # Escreve o arquivo csv
        with open(os.getcwd() + '/csv/' + os.path.splitext(file)[0] + '.csv', mode='w') as csv_file:
            header = ['arquivo', 'quant circulo']

            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()

            writer.writerow({'arquivo': file, 'quant circulo': len(circles)})

            fieldnames = ['X', 'Y', 'R']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            # Passa pelo (x, y) coordenadas e o raio dos circulos
            for (x, y, r) in circles:
                # Desenha o circulo na output image, e então desenha um retangulo
                # correspondendo o centro do circulo
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5),
                              (x + 5, y + 5), (0, 128, 255), -1)
                # print("X,Y do centro do circulo" + str((x, y)))
                writer.writerow({'X': x, 'Y': y, 'R': r})

    else:
        # print("Nenhum circulo encontrado no aquivo " + file)

        # Escreve o arquivo csv
        with open(os.getcwd() + '/csv/' + os.path.splitext(file)[0] + '.csv', mode='w') as csv_file:
            header = ['arquivo', 'quant circulo']

            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()

            writer.writerow({'arquivo': file, 'quant circulo': 0})
