import cv2
vidcap = cv2.VideoCapture('videos/video1.mp4')
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("imagens/frame%d.jpg" % count, image)     # Salva o frame como arquivo JPEG
    success, image = vidcap.read()
    # print('Lendo um novo frame: ', success)
    count += 1
