"""
test.py
---------
prototyping file for Dexter and Nathans machine learning final project
---------
"""

from sampleExtraction import *
from wave import *
from pyConvert import convert
from stft import *
from rect import *
import matplotlib.pyplot as plt
from onset import *
from smooth import *
import numpy as np
from mfcc import *
from supervised import *
from scipy.io import wavfile
from features import *

featureNumber = 11

"""
----------------------------------
Proto-functions
----------------------------------
"""

"""
---------------------------------
Test Code for Program
--------------------------------
"""
#read the file and get the mono data and sample rate returned
pureData, srate = convert('clips/drumLoop.wav', 1)
#plot it
plt.subplot(211)
plt.plot(pureData)
plt.title('Converted, pre')
#preprocessing
"""
remove DC onset, energy,  normalize, half-wave rect
"""
#dataSegment = pureData[32*srate:35.8*srate]#take seconds 35-35.8 from the piece to use from here on out
data = removeDC(pureData)
data = normalAverage(data)
data = fullWave(data)
#data = energy(data)
#data = normalized(data)


#lets plot this shit
plt.subplot(212)
plt.plot(data)
plt.title('After pre-Processing :')
#plt.show()

#The only work that needs to be done for the preprocessing is adding the option for down sampling
#we dont really need it but it might make things work better down the line

"""
Onset Detection Section :
"""
print("---------------------")
print("Entering Onset Detection Section")
print("---------------------")
onsets = np.zeros(len(data))
onsets = localMax(data, srate)
samples = extractSamples(pureData, srate, onsets)
print("Number of Samples :", len(samples))
#print("Length of Sample 5 :", len(samples[4]))

#The onset detection code is quite wonky
#this is the weakest part of the code that is written so far
#we need to implement a more effective system for onset detection besides local max

"""
Feature Extraction Section :
"""
print("----------------------")
print("Entering Feature Extraction Section ")
print("----------------------")
#note that ZCR is taken during onset section of
f_ZCR = np.zeros(len(samples))
f_RMS = np.zeros(len(samples))
f_HFC = np.zeros(len(samples))
f_lowRMS = np.zeros(len(samples))
f_midRMS = np.zeros(len(samples))
f_highRMS = np.zeros(len(samples))
f_spectralFlux = np.zeros(len(samples))
f_lv = np.zeros(len(samples))
f_mv = np.zeros(len(samples))
f_hv = np.zeros(len(samples))
f_lvm = np.zeros(len(samples))
f_lvh = np.zeros(len(samples))
f_mvh = np.zeros(len(samples))

for i in range (len(samples)):
    X = myFFT(samples[i])
    sampleLength(samples[i], srate)
    print("Extracting Features from sample ", i)
    f_ZCR[i] = xCrossingCount(samples[i])
    print("Zero Crossing Count : ", f_ZCR[i])
    f_RMS[i] = RMS(samples[i])
    print("RMS 1-Band : ", f_RMS[i])
    f_lowRMS[i], f_midRMS[i], f_highRMS[i], f_lv[i], f_mv[i], f_hv[i], f_lvm[i],  f_lvh[i], f_mvh[i] = threeBandRMS(samples[i])
    print("RMS 3-Band Isolated Bands : ", f_lowRMS[i], ",",f_midRMS[i], " ", f_highRMS[i])
    print("Band Vs All : ", f_lv[i], f_mv[i], f_hv[i])
    print("Band Vs Others : ", f_lvm[i], f_lvh[i], f_mvh[i])
    f_spectralFlux[i] = spectralFlux(samples[i])
    print("Spectral Flux : ", f_spectralFlux[i])
    #f_HFC[i] = hfc(X)
    #print("HFC : ", f_HFC[i])

#spectral kurtosis -
#RMS (3band vs 1 band) - not sure if we need this..
#Temp Centroid
#Spectral Centroid

"""
Machine Learning Section :
"""
print("----------------------")
print("Entering Machine Learning Section")
print("----------------------")

#need to create np array with n dimentions where n is the number of features + 1
#the first dimention of the array should contain the raw audio data, all the other dimentions are the different features we have
#next we send this to the SVM function inside the supervised.py file
#tweak the variable and we should hopfully have the machine learning finished
"""
Exporting Sectio
"""
print("----------------------")
print("Entering Sample Exportion Section")
print("----------------------")
exportSamples(samples)
