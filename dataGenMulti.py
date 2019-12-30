import threading
from queue import Queue
from gtts import gTTS
import pandas as pd

LABELPATH = 'C:\\Data\\bn_bd\\line_index.tsv'
SAVEPATH = 'C:\\Data\\bn_bd\\synthWav\\'
max_threads = 100

def getWav(q):
    while True:
        info = q.get()
        fileID = info[0]
        text = info[1]
        print('Requesting TTS for file: ' + fileID)
        tts = gTTS(text, lang='bn')
        print('TTS Complete, Saving ...')
        tts.save(SAVEPATH + fileID + '_synth.wav')
        print(fileID + ': Complete')
        q.task_done()

que_files = Queue()

df = pd.read_csv(LABELPATH,delimiter='\t', header = None)

for i in range(max_threads -1):
    t = threading.Thread(target = getWav, args = (que_files,))
    t.setDaemon(True)
    t.start()

for index, row in df.iterrows():
    que_files.put(row)

que_files.join()