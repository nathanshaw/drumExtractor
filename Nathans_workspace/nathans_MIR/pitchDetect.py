"""
pitchDetect.py
-----------------
A Group of Functions for Detecting and Manipulating Pitch in
Audio Files
-----------------------------------------
Author   :    Nathan Villicana-Shaw
Email    :    nathanshaw@alum.calarts.edu
Data     :    october 13, 2014

CalArts  : MTEC-480
Fall 2014
-----------------
"""

import numpy as np
from scipy.fftpack import fft, ifft, rfft
from matplotlib.pyplot import *
from scipy.signal import get_window

def onsetFFT(x, onsets,N, sRate):
    """
    --------------------
    Calculates the frequencies of a group of note onsets passed to function
    --------------------
    Variables :
    --------------------
    x         : incomming array of audio data
    onsets    : incomming array that flags onsets in x with 1's
    N         : window size of fft analysis
    sRate     : sample rate of the audio data
    --------------------
    Returns   :
    --------------------
    windows   : array of frequency values corrisponding with onsets
    --------------------
    """
    onsetNum = 0
    note = 0
    for i in range(0,len(onsets)):
            if (onsets[i] == 1):
                onsetNum = onsetNum + 1
    windows = np.zeros(len(onsetNum))
    for i in range(0,len(onsets)):
        if (onsets[i] == 1):
            windows[note] = fft(x[i,i+N])
            note = note + 1
    return windows

def fftFreq(x, sRate):
    """
    --------------------
    calculates the windowed FFT of a given chunk
    --------------------
    Variables :
    --------------------
    x          :  incomming array of audio data
    --------------------
    Returns :
    --------------------
    freq       :  the dominate frequency in the sample passed into the function
    --------------------
    """
    win = 'hann'
    windowedX = x * get_window(win,len(x))
    X = rfft(windowedX)
    freq = np.argmax(X)#should interpolate for more accuracy
    freq = sRate * freq / len(x)
    return freq

"""
--------------------
Some works in progress ...
--------------------
def fftExtraction1(x, srate):

    --------------------
    function for extracting specific frequencies from an ancomming array of audio data
    --------------------
    Variables  :
    --------------------

    --------------------
    Returns    :
    --------------------

    --------------------

    X = fft(x)
    m = np.zeros(len(X))
    m[800:1200] = np.linspace(0,1,400)
    m[1200:] = 1
    m[-1200:] = m[1200:0:-1]
    plot(m)
    y = real(ifft(X*m))
    snd.play(srate,y)
    return 0

def autoCorr(x):
    #diff = np.var(x)
    #x = x - np.mean(x)
    X = np.correlate(x,x,mode = 'full')[-len(x):]#starts procress by analyzing the last sample with the firist
    return X[:len[X]//2]

def HPS(x, srate, win=None):
    if win is None:
        win = 'hann'
    windowedX = x*get_window(win,len(x))
    realX = abs(rfft(windowedX))
    """
