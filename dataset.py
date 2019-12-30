import pandas as pd
from scipy.io import wavfile
import librosa
import numpy as np

LABELPATH = 'C:\\Data\\bn_bd\\line_index.tsv'
TARGETPATH = 'C:\\Data\\bn_bd\\wavs\\'
INPUTPATH = 'C:\\Data\\bn_bd\\wavOut\\'

df = pd.read_csv(LABELPATH, delimiter='\t', header = None)

N = df.shape[0]

targetShapes = []
inputShapes = []

for index, row in df.iterrows():
    print('processing: ' + str(index+1) + ' of ' + str(N))
    fileID = row[0]
    dataTarget, fst = librosa.load(TARGETPATH + fileID + '.wav', sr = 8000)
    dataInput, fsi = librosa.load(INPUTPATH + fileID + '_synth.wav', sr = 8000)
    targetShapes.append(dataTarget.shape[0])
    inputShapes.append(dataInput.shape[0])

targetShapes = np.asarray(targetShapes)
inputShapes = np.asarray(inputShapes)

data = [targetShapes, inputShapes]
data = np.asarray(data).transpose()
shapeDf = pd.DataFrame(data)
shapeDf.to_csv('summary.csv')