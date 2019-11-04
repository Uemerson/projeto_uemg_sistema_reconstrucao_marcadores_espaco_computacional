import oct2py
import numpy as np
import cv2

oc = oct2py.Oct2Py()

Calib1 = oc.load('coord/larissa/Calib1.mat', '-ascii')
Calib2 = oc.load('coord/larissa/Calib2.mat', '-ascii')
Calib3 = oc.load('coord/larissa/Calib3.mat', '-ascii')
Calib4 = oc.load('coord/larissa/Calib4.mat', '-ascii')

GRID = oc.load('coord/Grid3.mat', '-ascii')

oc.addpath('/')

CAM1_CALIB = oc.CalibrationDLT(Calib1.transpose(), GRID.transpose())
CAM2_CALIB = oc.CalibrationDLT(Calib2.transpose(), GRID.transpose())
CAM3_CALIB = oc.CalibrationDLT(Calib3.transpose(), GRID.transpose())
CAM4_CALIB = oc.CalibrationDLT(Calib4.transpose(), GRID.transpose())

Pontos1_ = oc.load('coord/larissa/PontosCam1Quadro68.m', '-ascii')
Pontos2_ = oc.load('coord/larissa/PontosCam2Quadro68.m', '-ascii')
Pontos3_ = oc.load('coord/larissa/PontosCam3Quadro68.m', '-ascii')
Pontos4_ = oc.load('coord/larissa/PontosCam4Quadro68.m', '-ascii')

Paparece = oc.Paparece(Pontos1_, Pontos2_, Pontos3_, Pontos4_)
Pontos = oc.Pontos(Pontos1_, Pontos2_, Pontos3_, Pontos4_)
CAMS = oc.CAMS(CAM1_CALIB, CAM2_CALIB, CAM3_CALIB, CAM4_CALIB)

npontos = oc.size(Pontos1_,1)
CALC_CAMS = oc.zeros(4,1)

Pontos3D = oc.Pontos3D(npontos, Paparece, CALC_CAMS, CAMS, Pontos)

oc.Plot(GRID, Pontos3D)

# oc.plot([1,2,3],'-o', linewidth=2)
# plt.Plot(GRID, Pontos3D)

# matplotlib = py.matplotlib
#   plt = matplotlib.pyplot
#   plt.plot (rand (1, 1000))
#   plt.show()

# oc.Plot(GRID, Pontos3D)

# oc.plot([1,2,3],'-o', linewidth=2)
# pause(1)
# while True:
#     oc.Plot(GRID, Pontos3D)
    # k = cv2.waitKey(1) & 0xFF
    # # press 'q' to exit
    # if k == ord('q'):
    #     break
    # elif k == ord('b'):
    #     # change a variable / do something ...
    # elif k == ord('k'):
        # change a variable / do something ...

    # oc.plot(GRID, Pontos3D)
# oc.plot([1,2,3],'-o', linewidth=2)
