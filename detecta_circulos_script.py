import numpy as np
import argparse
import cv2

image = cv2.imread("imagens/frame0.jpg")
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Cnverte para escala de cinza

# Função do opencv para detectar circulos
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.4, 100)

# Verifica se foi encontrado algum circulo
if circles is not None:
    # Converte (x, y) coordenadas and raio do circulo para inteiro
    circles = np.round(circles[0, :]).astype("int")

    # Passa pelo (x, y) coordenadas e o raio dos circulos
    for (x, y, r) in circles:
        # Desenha o circulo na output image, e então desenha um retangulo
        # correspondendo o centro do circulo
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5),
                      (x + 5, y + 5), (0, 128, 255), -1)
        print("X,Y do centro do circulo" + str((x, y)))

cv2.imshow('original escala', image)

height, width, channels = image.shape

image = cv2.resize(image, (int(width/2), int(height/2)))
output = cv2.resize(output, (int(width/2), int(height/2)))

cv2.imshow('original', image)
cv2.imshow('output', output)
cv2.waitKey(0)
