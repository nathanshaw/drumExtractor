"""
--------------------
audioFeatures.py 
--------------------
A set of functions for extracting audio features
--------------------
"""
from scipy import *
import numpy as np
from preProcessing import *

def RMS(x):
    """
    ----------------------
    A function calculating the root means square of an array of data
    ----------------------
    Variables :
    ----------------------
    x     :   the input array of data
    ----------------------
    Returns
    ----------------------
    the RMS of x
    ----------------------
    """
    total = 0
    for i in range(len(x) - 1):
        total = x[i] + total
    return (total/len(x))**(0.5)

def threeBandRMS(X):
    """
    -----------------------
    function that splits FFT data into three equal chunks and compares the RMS values of the
    chunks returning 9 comparison features 
    -----------------------
    Variables :
    -----------------------
    X : input array of FFT data
    -----------------------
    Outputs :
    -----------------------
    low     : the amount of energy observed in the lower third frequency bins
    mid     : the amount of energy observed in the middle third frequency bins
    high    : the amount of energy observed in the higher third frequency bins
    LV      : ratio of energy contained in the lower third compared to other bins
    MV      : ratio of energy contained in the middle third compared to other bins
    HV      : ratio of energy contained in the higher third compared to other bins
    LVM     : lower third vs middle third
    LVH     : lower third vs higher third
    MVH     : middle third vs higher third
    -----------------------
    """
    low = RMS(X[:len(X)//3])
    mid = RMS(X[len(X)//3:(len(X)//3)*2])
    high = RMS(X[(len(X)//3)*2:])
    #one band vs energy of other two bands
    LV = low / ((mid + high)/2)
    MV = mid / ((low + high)/2)
    HV = high / ((mid + low)/2)
    #one band vs energy of other specific band
    LVM = low / mid
    LVH = low / high
    MVH =  mid / high
    #return the nine features from three band RMS
    return low, mid, high, LV, MV, HV, LVM, LVH, MVH

def spectralFlux(x, hop=None):
    """
    ----------------------
    A function for detecting the amount of relitive energy change in a signal
    ----------------------
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
    x = halfWave(x)
    #smooth out the data using the envelope function
    flux = envelope(x, hop)
    aver = flux[0]
    for i in range (hop, len(x) - hop, hop):
        flux[i:i+hop] = np.abs(flux[i] - flux[i+hop])
    for i in range (len(flux)):
       aver = aver + flux[i]

    return (aver/(len(flux)))

def zeroCrossings(x, srate = 44100):
    """
    ----------------------
    function that returns the zero crossing rate of an array of audio data
    as well as an array corrisponding to zero crossing points
    ----------------------
    Variables :
    ----------------------
    x         :  incoming array of audio data (or data in general
    srate     :  the sample rate of the incoming data
    ----------------------
    Returns
    ----------------------
    crossings    :  an np array where 1's populate points of zero crossing and 0's are all other samples
    crossingRate :  the number of crossings a second
    ----------------------
    """
    #used to keep track of number of overall crossings
    crossingCount = 0
    crossings = np.zeros(len(x))
    
    for i in range (1, len(x)):
        if ((x[i] > 0) & (x[i-1] <= 0)):
                crossings[i] = 1
                crossingCount = crossingCount + 1
        if ((x[i] < 0) & (x[i-1] > 0)):
                crossings[i] = 1
                crossingCount = crossingCount + 1

    crossingRate = (crossingCount*len(x)/srate/2)
    
    return crossings, crossingRate 

def envelope(x, binSize=None):
    """
    ----------------------
    function for determining the overall amplitude envelope of a signal
    ----------------------
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

