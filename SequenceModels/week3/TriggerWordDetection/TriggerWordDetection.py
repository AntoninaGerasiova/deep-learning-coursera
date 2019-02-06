import numpy as np
from pydub import AudioSegment
import random
import sys
import io
import os
import glob
import pyaudio  
import wave  
from td_utils import *

def play_wav(file_name):
    #define stream chunk   
    chunk = 1024  

    #open a wav format music  
    f = wave.open(file_name,"rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()  

if __name__ == "__main__":
    #x = graph_spectrogram("audio_examples/example_train.wav")
    play_wav("raw_data/activates/1.wav")
