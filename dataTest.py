DATAPATH = 'C:\\Data\\bn_bd\\'
LABELPATH = 'C:\\Data\\bn_bd\\line_index.tsv'

import os
import pandas as pd
from gtts import gTTS

os.listdir(DATAPATH)

df = pd.read_csv(LABELPATH,delimiter='\t', header = None)

for index, row in df.iterrows():
    fileID = row[0]
    text = row[1]
    break

tts = gTTS(text, lang='bn')
tts.save('test.mp3')