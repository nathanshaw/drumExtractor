"""
onset.py

---------------
A program for detecting event onsets
--------------

Author : Nathan Villicana-Shaw
Email  : nathanshaw@alum.calarts.edu
Date   : sep 30, 2014

CalArts : MTEC-480
Fall 2014


"""
import numpy as np
from smooth import *
from rect import *



def hfc(x):
    raise NotImplementedError()

def spectralFlux(x, hop=None):

    """
    A function for detecting the amount of relitive energy change in a signal
    -------------------
    Variables :
    ----------------------
    x     :   the input array of data
    hop   :   the number of samples to analyze at once
    ----------------------
    Returns
    ----------------------
    flux  :   the spectral flux of the signal
    ----------------------
    """
    if (hop == None):
        hop = 100
    flux = envelope(x, hop)

    x = halfWave(x)
    aver = flux[0]
    for i in range (hop, len(x) - hop, hop):
        flux[i:i+hop] = np.abs(flux[i] - flux[i+hop])
    return flux

def complexNovelty(x):
    """
    -------------------
    Variables :
    ----------------------
    ----------------------
    Returns
    ----------------------
    """
    raise NotImplementedError()

def zeroCrossingRate(x, srate = 44100):
    crossingCount = 0

    crossings = np.zeros(len(x))
    for i in range (1, len(x)):
        if ((x[i] > 0) & (x[i-1] <= 0)):
                crossings[i] = 1
                crossingCount = crossingCount + 1
        if ((x[i] < 0) & (x[i-1] > 0)):
                crossings[i] = 1
                crossingCount = crossingCount + 1

    print(crossingCount*len(x)/srate/2)
    return crossings

def envelope(x, binSize=None):
    """
    function for determining the overall amplitude envelope of a signal
    -------------------
    Variables :
    ----------------------
    x         :  incoming array of audio data (or data in general
    binSize   :  the amount of samples processed at a time
    ----------------------
    Returns
    ----------------------
    x         :  an array containing the envelope data
    """
    if (binSize == None):
        binSize = 2200
    for i in range(0,len(x)-binSize,binSize):
        maxi = 0.0
        for j in range (i,i+binSize):
            if (x[j] > maxi):
                maxi = x[j]
        for i in range(i,i+binSize):
            x[i] = maxi
    return x

def localMax(x, srate=None):
    """
    -------------------
    Detects amplitude peaks in given array of data (scaled)
    -------------------
    Variables :
    ----------------------
    x      :  incoming array of audio data (or data in general
    srate  :  the sample rate of the incomming signal - allows for more
              meaningful results
    ----------------------
    Returns
    ----------------------
    peaks  : An array consisting of the locations of the local peaks as found
            by functions
    ----------------------
    """
    print("Entering peakfinder1 function")
    if (x.ndim > 1):
        print("Please pass a mono file into peakDetect")
        return 1
    if (srate == None):
        srate = 44100
        print("No sample rate given, No Problem setting it to 44100")

    peaks = np.zeros(len(x))
    for i in range(1,len(x)-1):
        cond1 = x[i] > x[i-1]
        cond2 = x[i] > x[i+1]
        cond3 = x[i] > 0.16
        if (cond1 * cond2 * cond3 == True):
            peaks[i] = 1
    counter = 0
    for i in range(0,len(peaks)):
        if (peaks[i] > 0):
            if (srate/counter < 4000):#gets rid of freqs we dont expect
                print("Projected Frequency :",srate/counter)
                counter = 0
        else:
            counter = counter + 1

    return peaks

