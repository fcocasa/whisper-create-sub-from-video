import os
import torch
import whisper
import moviepy.editor
from datetime import datetime, timedelta
import os
from time import time
from tkinter.filedialog import askopenfilename

filename = askopenfilename()
VIDEO_FILE = filename
print("Video:",VIDEO_FILE)
SPEECH_FILE = ".".join(VIDEO_FILE.split('.')[:-1]) + '.mp3'
print("Audio:",SPEECH_FILE)
SRT_FILE = ".".join(VIDEO_FILE.split('.')[:-1]) + '.srt'
print("Subtitulos:",SRT_FILE)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device: ",device)

print('Pasando video a audio...')
video = moviepy.editor.VideoFileClip(VIDEO_FILE)
if not os.path.isfile(SPEECH_FILE):
    video.audio.write_audiofile(SPEECH_FILE)

print('Cargando el modelo whisper...')
model = whisper.load_model('small').to(device)

s = time()
print('Transcribiendo...')
result = model.transcribe(SPEECH_FILE)
print('Tiempo tomado en transcribir (minutos):',(time()-s)/60)

print('Creando los subtitulos...')
srt = ''
hour_minute_second= ('%02d:%02d:%02d'%(0,0,0))
contador_tiempo = datetime.strptime(hour_minute_second,'%H:%M:%S')

for index, value in enumerate(result['segments']):
    sub = f'''{index}
'''
    sub += f'{(contador_tiempo + timedelta(seconds=float(value["start"]))).strftime("%H:%M:%S")},000 --> '
    
    # contador_tiempo = contador_tiempo + timedelta(0,value['end']-value['start'])

    sub += f'''{(contador_tiempo  + timedelta(seconds=float(value["end"]))).strftime('%H:%M:%S')},000
'''
    
    sub += value['text']
    sub += '''

'''    
    srt += sub

with open(SRT_FILE,'w+') as file:
    file.write(srt)