import pandas as pd
from scipy.io import wavfile
import librosa
import numpy as np
import h5py

LABELPATH = 'C:\\Data\\bn_bd\\line_index.tsv'
TARGETPATH = 'C:\\Data\\bn_bd\\wavs\\'
INPUTPATH = 'C:\\Data\\bn_bd\\wavOut\\'
dbPath = 'C:\\Data\\bngan5s.h5'

df = pd.read_csv(LABELPATH, delimiter='\t', header = None)

ntotal = df.shape[0]
N = 849

db = h5py.File(dbPath, mode = 'w')
db.create_dataset("fileID", (N,), np.dtype('|S16'))
db.create_dataset("target", (N, 40000), np.float32)
db.create_dataset("input", (N, 40000), np.float32)

#fileID = df.iloc[31][0]
idx = 0

for index, row in df.iterrows():
    print('processing: ' + str(index+1) + ' of ' + str(ntotal))
    fileID = row[0]
    dataTarget, fst = librosa.load(TARGETPATH + fileID + '.wav', sr = 8000)
    dataInput, fsi = librosa.load(INPUTPATH + fileID + '_synth.wav', sr = 8000)
    target = np.zeros(40000)
    input = np.zeros(40000)
    if((dataInput.shape[0] <= 40000) and (dataTarget.shape[0] <= 40000)):
        print('writing to Database')
        target[:dataTarget.shape[0]] = dataTarget
        input[:dataInput.shape[0]] = dataInput
        db["fileID"][idx] = np.asarray(fileID, dtype = np.dtype('|S16'))
        db["target"][idx] = target
        db["input"][idx] = input
    else:
        print('sample size > 5 s, skipping')

db.close()