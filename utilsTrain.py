import h5py
import numpy as np
#from tensorflow.keras.utils import to_categorical
import os

# to test generator, values = next(generator) in code

def ensureDir(filePath):
	
	''' This function checks if the folder at filePath exists.
		If not, it creates it. '''

	if not os.path.exists(filePath):
		os.makedirs(filePath)

def generator(h5file, indexes, batch_size):
    X = []
    Y = []
    idx = 0
    while True:
        for index in indexes:
            input = np.expand_dims(h5file["input"][index], axis = -1)
            target = np.expand_dims(h5file["target"][index], axis = -1)
            X.append(input)
            Y.append(target)
            idx = idx + 1
            if(idx>=batch_size):
                yield np.asarray(X),np.asarray(Y)
                idx = 0
                X = []
                Y = []