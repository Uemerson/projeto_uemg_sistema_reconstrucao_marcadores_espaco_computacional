import oct2py
import numpy as np
import cv2

oc = oct2py.Oct2Py()
CAM1_CALIB = None
CAM2_CALIB = None
CAM3_CALIB = None
CAM4_CALIB = None
GRID = None

def calibCams(pathCams, pathWorld):
    global oc
    global CAM1_CALIB
    global CAM2_CALIB
    global CAM3_CALIB
    global CAM4_CALIB
    global GRID

    CAM1_CALIB = None
    CAM2_CALIB = None
    CAM3_CALIB = None
    CAM4_CALIB = None
    GRID = None

    try:
        Calib1 = oc.load(pathCams[0], '-ascii')
        Calib2 = oc.load(pathCams[1], '-ascii')
        Calib3 = oc.load(pathCams[2], '-ascii')
        Calib4 = oc.load(pathCams[3], '-ascii')

        GRID = oc.load(pathWorld, '-ascii')

        oc.addpath('/')

        CAM1_CALIB = oc.CalibrationDLT(Calib1.transpose(), GRID.transpose())
        CAM2_CALIB = oc.CalibrationDLT(Calib2.transpose(), GRID.transpose())
        CAM3_CALIB = oc.CalibrationDLT(Calib3.transpose(), GRID.transpose())
        CAM4_CALIB = oc.CalibrationDLT(Calib4.transpose(), GRID.transpose())

        print(CAM1_CALIB)
        print(CAM2_CALIB)
        print(CAM3_CALIB)
        print(CAM4_CALIB)
    
    except:
        raise ValueError('Ocorreu um erro ao tentar calibrar as coordenadas')
    
def calibPoints(pathPoints):
    global oc
    global CAM1_CALIB
    global CAM2_CALIB
    global CAM3_CALIB
    global CAM4_CALIB
    global GRID

    if (CAM1_CALIB is None) or (CAM2_CALIB is None) or (CAM3_CALIB is None) or (CAM4_CALIB is None) or (GRID is None):
        raise Exception('NotCalib')

    Pontos1_ = oc.load(pathPoints[0], '-ascii')
    Pontos2_ = oc.load(pathPoints[1], '-ascii')
    Pontos3_ = oc.load(pathPoints[2], '-ascii')
    Pontos4_ = oc.load(pathPoints[3], '-ascii')

    Paparece = oc.Paparece(Pontos1_, Pontos2_, Pontos3_, Pontos4_)
    Pontos = oc.Pontos(Pontos1_, Pontos2_, Pontos3_, Pontos4_)
    CAMS = oc.CAMS(CAM1_CALIB, CAM2_CALIB, CAM3_CALIB, CAM4_CALIB)

    npontos = oc.size(Pontos1_,1)
    CALC_CAMS = oc.zeros(4,1)

    Pontos3D = oc.Pontos3D(npontos, Paparece, CALC_CAMS, CAMS, Pontos)
    oc.Plot(GRID, Pontos3D)
