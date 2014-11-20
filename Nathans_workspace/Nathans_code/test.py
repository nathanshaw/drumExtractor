"""
test.py
---------
prototyping file for Dexter and Nathans machine learning final project
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
from supervised import *
from scipy.io import wavfile

"""
----------------------------------
Proto-functions
----------------------------------
"""
def extractFeatures(sample, srate):
    """
    Function that takes in individual samples and extracts a set of features about that sample

    Returns :
        A list of features, and the sample passed into it
    """


def extractSamples(data, srate, onsets):
    """
    Function for extracting samples from data with a list of onsets
    """
    sampleList = []
    sampNum = 0
    for i in range(len(data)-1):
        if onsets[i] == 1:#if we found a peak
            found = 0
            start = i#set start to that sample
            #lets find the next onset
            for j in range(i+1, i + srate):#if there is another onset within a third of a second
                if j < len(data)-1:
                    if onsets[j] == 1:
                        end = j + i
                        found = 1
            if found == 0:
                end = i+(srate)
            #load up the sample data into a NP array
            sampleList.append(data[start:end])
            sampNum = sampNum + 1
    #print('----------------')
    #print(sampleList)
    print('----------------')
    print(sampNum, ' samples extracted')
    print('----------------')
    return sampleList


"""
---------------------------------
Test Code for Program
--------------------------------
"""


#read the file and get the mono data and sample rate returned
data, srate = convert('clips/Rainspiration.wav', 1)
#plot it
plt.subplot(211)
plt.plot(data)
plt.title('Converted, pre')
#preprocessing
"""
remove DC onset, energy,  normalize, half-wave rect
"""
data = data[35*srate:35.8*srate]#take seconds 35-35.8 seconds from the piece to use from here on out
data = removeDC(data)
data = halfWave(data)
data = energy(data)
data = normalized(data)
#lets plot this shit
plt.subplot(212)
plt.plot(data)
plt.title('After pre-Processing :')
#plt.show()
#onset detection
"""
returns np.array with onset labels
"""
onsets = np.zeros(len(data))
onsets = localMax(data, srate)
samples = extractSamples(data, srate, onsets)
print("Number of Samples :", len(samples))
print("Length of Sample 5 :", len(samples[4]))

#feature extraction of onset-onset
"""
STFT = >
HFC
spectral kurtosis
RMS (1 band)
RMS (3band)
RMS (3band vs 1 band)
zero crossing rate
Temp
Centroid
Spectral Centroid

"""
f_spectFlux = spectralFlux(data)
#features and labels are pumped into SVM learning algorithm for classification
"""

"""
#export classified data as clips


#imshow(mfcc(stft(data),srate, 2048))
#def imshow(X):
#    plt.imshow(X, aspect='auto',origin='lower',interpolation='nearest')
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
