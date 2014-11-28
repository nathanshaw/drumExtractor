"""
test.py
---------
prototyping file for Dexter and Nathans machine learning final project
---------
"""
from wave import *
from pyConvert import convert
from stft import *
from rect import *
import matplotlib.pyplot as plt
from onset import *
from smooth import *
from pitchDetect import *
import numpy as np
from mfcc import *
from supervised import *
from scipy.io import wavfile
from features import *
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

def exportSamples(samples, label=None):
    """
    Function for Exporting Arrays of Audio data as labeled .wav files
    -----------------
    Variables
    -----------------
    samples = incomming array of audio data
    label   = incomming array with labels for incomming audio data
            The function assumes the following :
                0 = data is not percussive, function discards the sample
                1 = data is percussive but of unknown catagory
                2 = data is catagorized as a Kick Drum
                3 = data is catagorized as a Snare
                4 = data is catagorized as a Clap
    -----------------
    Returns :
    -----------------

    -----------------
    """
    if (label == None):
        print("No label data given, will export all samples with unknown type")
        for i in range(len(samples)):
            sampleName = nameFile(1) + str(i)
            #export samples[i]
        return 0

    for i in range(len(samples)):
        sampleName = nameFile(label[i])
        createWave(samples[i])
    return 0

def createWave(sample):
    Wave_write.writeframes(sample)


def nameFile(label):
    if (label == 0):
        fileName = 'tonal'
    if (label == 1):
        fileName = 'unknown'
    if (label == 2):
        fileName = 'Kick'
    if (label == 3):
        fileName = 'Snare'
    if (label == 4):
        fileName = 'Clap'
    return fileName

onsets = np.zeros(len(data))
onsets = localMax(data, srate)
samples = extractSamples(data, srate, onsets)
print("Number of Samples :", len(samples))
print("Length of Sample 5 :", len(samples[4]))
#feature extraction of onset-onset
RMS = RMS(data)
print("RMS 1-Banf : ", RMS)
lowRMS, midRMS, highRMS = threeBandRMS(data)
#HFC
#spectral kurtosis
#RMS (3band vs 1 band)
#zero crossing rate
#Temp
#Centroid
#Spectral Centroid
f_spectFlux = spectralFlux(data)
print("Spectral Flux : ", f_spectFlux)
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
