"""
preProcessing.py
-------------------
A group of preProcessing functions for DSP
--------------------------
Author          : Nathan Villicana-Shaw
Email           : nathanshaw@alum.calarts.edu
Date            : December 9th,, 2014
--------------------------
CalArts : MTEC-480
Fall 2014
--------------------------
"""

import numpy as np
from scipy.signal import lfilter, firwin, medfilt
from pylab import figure, plot, grid, show

def lpf(x, sens):
    """
    --------------------
    Low Pass Filter Function
    --------------------
    Variables :
    --------------------
    x    :   Incomming array of audio data
    sens :   the number of samples the function looks back to in order to filter the data
    --------------------
    Returns :
    --------------------
    x    :   The data filtered from x + sens to the last sample
    --------------------
    """
    for i in range(sens, len(x)):
        for s in range(1, sens):
            x[i] = (x[i-s] + x[i])
        x[i] = x[i]/sens
    return x

def normalized(x):
    """
    -------------------
    Normalizing Filter for scaling data in incomming array so the max value is equal to 1
    --------------------
    Variables :
    --------------------
    x    :   Incomming array of audio data
    --------------------
    Returns :
    --------------------
    X    :   The data filtered from x + sens to the last sample
    --------------------
    """
    maxi = 0
    X = np.zeros(len(x))
    for i in range(0, len(x)):
        if (x[i] > maxi):
            maxi = float(x[i])
    for i in range(0,len(x)):
        X[i] = x[i]/maxi
    return X

def normalAverage(x, windowSize = 21):
    """
    -------------------
    another type of low pass filter, this one looks ahead and behing to calculate value
    --------------------
    Variables :
    --------------------
    x          :   Incomming array of audio dataA
    windowSize :   the number of samples to use in order to calculate the average
    --------------------
    Returns :
    --------------------
    X    :   The data filtered from x + sens to the last sample
    --------------------
    """
    if (windowSize % 2 == 0):
        print("please enter in an odd number for window size next time")
    halfHop = (windowSize - 1)//2
    for i in range(halfHop, len(x) - halfHop):
        total = 0
        average = 0
        for i in range(-halfHop, halfHop):
            total = total + x[i]
        average = total/windowSize
        x[i] = average
    return x

def overSample(x):
    """
    -------------------
    an over sampler used for increading the number of samples available for calculation
    function interpolates between each sample to calculate a values between the two given
    --------------------
    Variables :
    --------------------
    x          :   Incomming array of audio dataA
    --------------------
    Returns :
    --------------------
    X    :   the incomming array x but twice as long
    --------------------
    """
    X = np.zeros[len(x)*2]
    for i in range (0, len(X)):
        if (i % 2 == 0):
            X[i] = x[i/2]
        else :
            X[i] = (x[(i-1)/2] + x[(i+1)/2])/2
    return X

def underSample(x):
    """
    -------------------
    A undersampling function that takes all the even samples from the incomming array and returns them
    -------------------
    Variables :
    -------------------
    x : incomming array or list of data
    -------------------
    Returns   :
    -------------------
    X :  under sampled version of x
    -------------------
    """
    under = np.zeros(len(x)//2)
    for i in range(len(under)-1):
        under[i] = (x[i*2])
    return under

#this function needs some work
def highPass(x, cuttoff=4000):
    """
    -------------------
    a high pass filter that uses fft and ifft to remove frequencies above a threshold
    --------------------
    Variables :
    --------------------
    x          :   Incomming array of audio dataA
    cuttoff    :   the frequency where the filter will be in full effect
               :   default value : 4000
    --------------------
    Returns :
    --------------------
    filtered    :   x returned without any frequencies above the given cuttoff
    --------------------
    """
    f = np.zeros(len(x))#f is the filter
    f[cuttoff*3//4:cuttoff] = np.linspace(0,1,(cuttoff//4))#create a window that acts as filter
    f[cuttoff:] = 1#i dont think this works
    fftAnal = np.fft.rfft(x)
    print("Length of fftAnal  is :",len(fftAnal))
    print("Length of x is : ", len(x))
    for i in range(0, len(fftAnal)):
        fftAnal[i] = fftAnal[i] * f[i]
    filtered = np.fft.ifft(fftAnal)
    return filtered

def fir(x, srate=None, cutoffFreq=None, numTaps=None):
    """
    -------------------

    --------------------
    Variables :
    --------------------
    x          :   Incomming array of audio dataA
    srate      :   the sample rate of x
    cutoffFreq :   the frequency where the filter takes full effect
    numTaps    :   the length of the filter
    --------------------
    Returns :
    --------------------
    X    :   The data filtered
    --------------------
    """
    if (srate == None):
        srate = 44100

    nyquist = srate/2

    if (cutoffFreq == None):
        cutoffFreq = 4168#the frequency of c8
    if (numTaps == None):
        numTaps = 29 #filter length

    fir_coeff = firwin(numTaps, cutoffFreq/nyquist)#creates lowpass filter using FIR

    X = lfilter(fir_coeff, 1.0, x)

    return X

def removeDC(x):
    """
    ------------------------
    Function for calculating an array of datas DC bias and
    then removing it from the signal
    ------------------------
    Variables
    ------------------------
    x       : An array of data passed into finction
    ------------------------
    Returns :
    ------------------------
    X       : x returned after DC bias is removed from each sample
    ------------------------
    """
    total = 0
    X = np.zeros(len(x))
    bias = mean(x)
    print("removing signal bias of : ", bias)
    for i in range(0, len(x)):
        X[i] = x[i] - bias
    return X

def mean(x):
    """
    -------------------
    takes the arithmatic mean of the input array of data
    --------------------
    Variables :
    --------------------
    x          :   Incomming array of audio data
    --------------------
    Returns :
    --------------------
    X    :   The average of all the values with the array x
    --------------------
    """
    total = 0
    X = np.zeros(len(x))
    for i in range(0,len(x)):
        total = total+x[i]
    mean = total/len(x)
    return mean

def halfWave(x):
    """
    ---------------------------
    The function throws away all negative values in the input
    array
    ---------------------------
    Variables :
    ---------------------------
        x : array of data
    ---------------------------
    Returns :
    ---------------------------
        x : rectified array
    ---------------------------
    """
    for i in range(0, len(x)):
        if (x[i] <= 0):
            x[i] = 0
    return x

def fullWave(x):
    """
    -----------------------------
    The function ensures all values are positive
    -----------------------------
    Variables:
    -----------------------------
        x  :  array of data
    -----------------------------
    Returns  :
    -----------------------------
        x  :  rectified array
    -----------------------------
    """
    for i in range(0,len(x)):
        if (x[i] <= 0):
            x[i] = x[i]*-1
    return x

def energy(x):
    """
    ------------------------------
    The function takes the 'power' of the input signal by squaring the values
    ------------------------------
    Variables:
    ------------------------------
        x  :  array of data
    ------------------------------
    Returns  :
    ------------------------------
        x  :  rectified array given as power
    ------------------------------
    """
    for i in range(0, len(x)):
        x[i] = x[i]**(1/2)
    return x

def internalClip(x, threshold = None):
    """
    -----------------------
    An internal clipper function that only keeps the peaks of an incomming signal
    -----------------------
    Variables     :
    -----------------------
        x         :  incomming array of audio data
        threshold :  the minumum threshold for a signal to pass through the function
    -----------------------
    Returns       :
    -----------------------
        x         :  the clipped data is returned
    -----------------------

    """
    if threshold=None:
        threshold = 0.16

    x = smooth.normalize(x)

    for i in range(0, len(x)):
        if (x[i] < threshold):
            if(x[i] > -threshold):
                x[i] = 0
    return x

def binaryClip(x, threshold = None):
    """
    -----------------------
    An internal clipper function that only keeps the peaks of an incomming signal
    This clipper only returns -1,0 or 1. I call it a binary clipper
    -----------------------
    Variables     :
    -----------------------
        x         :  incomming array of audio data
        threshold :  the minumum threshold for a signal to pass through the function
    -----------------------
    Returns       :
    -----------------------
        x         :  the clipped data is returned as 1's, -1's or 0's
    -----------------------

    """
    if threshold=None:
        threshold = 0.16
    #normalize the data
    x = smooth.normalize(x)
    for i in range(0, len(x)):
        if (x[i] < threshold):
            if(x[i] > -threshold):
                x[i] = 0
        if (x[i] > 0):
            x[i] = 1
        if (x[i] < 0) :
            x[i] = -1
    return x


 def envelope(x, binSize=None):
     """
     ---------------------
     function for determining the overall amplitude envelope of a signal
     ---------------------
     Variables :
     ----------------------
     x         :  incoming array of audio data (or data in general
     binSize   :  the amount of samples processed at a time
     ----------------------
     Returns :
     ----------------------
     x         :  an array containing the envelope data
     ----------------------
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
