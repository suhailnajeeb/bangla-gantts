LABELPATH = 'C:\\Data\\bn_bd\\line_index.tsv'
SAVEPATH = 'C:\\Data\\bn_bd\\synth\\'

import os
import pandas as pd
from gtts import gTTS

df = pd.read_csv(LABELPATH,delimiter='\t', header = None)

NSAMPLES = df.shape[0]

for index, row in df.iterrows():
    try:
        fileID = row[0]
        text = row[1]
        print('Requesting TTS for file: ' + fileID + ' (' + str(index + 1) + ' of ' + str(NSAMPLES) + ')')
        tts = gTTS(text, lang='bn')
        print('TTS Complete, Saving ...')
        tts.save(SAVEPATH + fileID + '_synth.mp3')
        print(fileID + ': Complete')
    except:
        print('Failed to generate TTS for index: ' + str(index)) 