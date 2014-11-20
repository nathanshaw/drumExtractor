"""
smooth.py
--------------
A group of functions for smoothing, filtering, averaging and otherwise treating
incomming audio data
--------------
Author    : Nathan Villicana-Shaw
Email     : nathanshaw@alum.calarts.edu
Date      : Oct 13, 2014

CalArts   : MTEC-480
Fall 2014
--------------
"""
import numpy as np
from scipy.signal import lfilter, firwin, medfilt
from pylab import figure, plot, grid, show

def lpf(x, sens):
    """
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
            x[i] = (x[i-s] + x[i])/2
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
            maxi = x[i]
    multi = 1/maxi#rate to multiply each sample by
    for i in range(0,len(x)):
        X[i] = multi*x[i]
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
    X    :   The data filtered from x + sens to the last sample
    --------------------
    """
    X = np.zeros[len(x)*2]
    for i in range (0, len(X)):
        if (i % 2 == 0):
            X[i] = x[i/2]
        else :
            X[i] = x[(i-1)/2]/2 + x[(i+1)/2]
    return X

#not tested yet
def underSample(x, ratio=2):
    under = np.zeros(len(x)//ratio)
    for i in range(0,len(under)):
        under[i] = (x[i*ratio:i*ratio+ratio])/ratio
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
"""

----------
These Functions need more work : :
---------

def median(x, kernal = None):
    if (kernal == None):
        kernal = 5
    return (medfilt(x, kernal))

def weightedAverage(x, windowSize = 21):
    if (windowSize % 2 == 0):
        print("please enter in an odd number for window size next time")
    halfHop = (windowSize - 1)//2
    weight = 0
    for i in windowSize:
        weight = weight + i
    for i in range(halfHop, len(x) - halfHop):
        total = 0
        average = 0
        for i in range(-halfHop, halfHop):
            total = total + x[i]
        average = total/windowSize
        x[i] = average
    return x
"""

