import CalibrationDLT
import numpy as np
import h5py

f = h5py.File('somefile.mat','r')
data = f.get('data/variable1')
data = np.array(data) # For converting to a NumPy array

Calib1 = h5py.File('coord/larissa/Calib1.mat', 'r')
