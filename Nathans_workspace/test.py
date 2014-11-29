"""
test.py
---------
prototyping file for Dexter and Nathans machine learning final project
---------
"""

#from sampleExtraction import *
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
        label = np.ones(len(samples))

    sampleNames = nameFiles(label)
    for i in range(len(samples)):
        createWave(samples[i], sampleNames[i])
    return 0

def createWave(sample, fileName, srate):
    wavFile = wave.open(fileName, 'w')
    wavFile.setParams((1, 2, srate, 0, 'NONE', 'not compressed'))
    maxVol = 2**15-1.0
    wavFileData = ""
    for i in range(len(sample)):
        wavFileData += pack(sample[i])
    wavFile.writeframes(wavFileData)
    wavFile.writeframes(sample)
    wavFile.close()

def nameFiles(label):

    """
    Variables : Counters for Exporting Files as Right Names
    """
    unknownCount = 0
    tonalCount = 0
    kickCount = 0
    snareCount = 0
    clapCount = 0
    fileName = [len(label)]
    for i in range(len(label)-1):
        print(i)
        if (label[i] == 0):
            fileName[i] = 'tonal' + str(tonalCount)
            tonalCount += 1
        if (label[i] == 1):
            fileName[i] = 'unknown' + str(unknownCount)
            unknownCount = unknownCount + 1
        if (label[i] == 2):
            fileName[i] = 'Kick' + str(kickCount)
            kickCount += 1
        if (label[i] == 3):
            fileName[i] = 'Snare' + str(snareCount)
            snareCount += 1
        if (label[i] == 4):
            fileName[i] = 'Clap' + str(clapCount)

    return fileName


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
plt.show()
#onset detection

"""
Onset Detection Section :
"""

onsets = np.zeros(len(data))
onsets = localMax(data, srate)
samples = extractSamples(data, srate, onsets)
print("Number of Samples :", len(samples))
print("Length of Sample 5 :", len(samples[4]))
#feature extraction of onset-onset

"""
Feature Extraction Section :
"""

RMS = RMS(data)
print("RMS 1-Banf : ", RMS)
lowRMS, midRMS, highRMS = threeBandRMS(data)
f_spectFlux = spectralFlux(data)
print("Spectral Flux : ", f_spectFlux)
#spectral kurtosis
#HFC
#RMS (3band vs 1 band)
#zero crossing rate
#Temp
#Centroid
#Spectral Centroid

#features and labels are pumped into SVM learning algorithm for classification

"""
Machine Learning Section :
"""

"""
Exporting Section :
"""
#export classified data as clips
#exportSamples(samples)
