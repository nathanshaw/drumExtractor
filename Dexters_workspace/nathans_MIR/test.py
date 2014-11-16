"""
test.py
---------
quick file for testing all my fft functions
---------
"""
from pyConvert import convert
from stft import *
from plotter import *
from rect import *
import matplotlib.pyplot as plt
from onset import *
from smooth import *
from pitchDetect import *
import numpy as np
from beatTrackers import *
from mfcc import *

data, srate = convert('clips/Rainspiration.wav', 1)

imshow(mfcc(stft(data),srate, 2048))
plt.show()
def imshow(X):
    plt.imshow(X, aspect='auto',origin='lower',interpolation='nearest')
#timePlt(binaryClip(data/2),32.8,33)
#timePlt(data,1,1.5)
#timePlt(highPass(data,16000),1.1.5)
#timePlt(highPass(data,8000),1.1.5)
#timePlt(highPass(data,4000),1.1.5)
#timePlt(energy(data),0,1)

#timePlt(autoCorr(data))
#print(fftFreq(data, srate))
#fftExtraction1(data,srate)
#timePlt(zeroCrossingRate(dcata), 0, 0.1)
#timePlt(spectralFlux(data, 82),0, 5)
#dataRect = fullWave(data)
#timePlt(dataRect)
#timePlt(data)
#fftPlt(stft(data))
#pPlt(localMax(data, srate),1, 5,15,0,0.5, srate)
#pPlt(envelope(data, 2205),1, 5,15,0,0.5, srate)
#timePlt(envelope(dataRect), 0,20,0,10)
#timePlt(localMax(data), 0,80,0,1.2)

