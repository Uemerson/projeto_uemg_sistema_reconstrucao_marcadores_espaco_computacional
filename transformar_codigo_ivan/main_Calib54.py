import CalibrationDLT
import numpy as np
import re
import loadFile

Calib1 = loadFile.load('coord/larissa/Calib1.mat')
Calib2 = loadFile.load('coord/larissa/Calib2.mat')
Calib3 = loadFile.load('coord/larissa/Calib3.mat')
Calib4 = loadFile.load('coord/larissa/Calib4.mat')

GRID = loadFile.loadFloat('coord/Grid3.mat')

CAM1_CALIB = CalibrationDLT.CalibrationDLT(np.transpose(Calib1), np.transpose(GRID))

# print(Calib1)
# print(np.transpose(Calib1))
# CAM2_CALIB = CalibrationDLT.CalibrationDLT(np.transpose(Calib2), np.transpose(GRID))
# CAM3_CALIB = CalibrationDLT(Calib3', GRID')
# CAM4_CALIB = CalibrationDLT(Calib4', GRID')