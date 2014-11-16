"""
rect.py
--------------------------
A group of rectifing functions to help other functions
--------------------------
Author          : Nathan Villicana-Shaw
Email           : nathanshaw@alum.calarts.edu
Date            : October 13th, 2014
--------------------------
CalArts : MTEC-480
Fall 2014
--------------------------
"""
import smooth as smooth
import numpy as np

def halfWave(x):
    """
    The function throws away all negative values in the input
    array

    Variables :
        x : array of data

    Returns :
        x : rectified array
    """
    for i in range(0, len(x)):
        if (x[i] <= 0):
            x[i] = 0
    return x

def fullWave(x):
    """
    The function ensures all values are positive

    Variables:
        x  :  array of data

    Returns  :
        x  :  rectified array

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
        x  :  array of data
    ------------------------------
    Returns  :
        x  :  rectified array given as power
    ------------------------------
    """
    for i in range(0, len(x)):
        x[i] = x[i]**2
    return x

def internalClip(x, threshold = 0.16):
    """
    -----------------------
    An internal clipper function that only keeps the peaks of an incomming signal
    -----------------------
    Variables     :
        x         :  incomming array of audio data
        threshold :  the minumum threshold for a signal to pass through the function
    -----------------------
    Returns       :
        x         :  the clipped data is returned
    -----------------------

    """
    x = smooth.normalize(x)
    for i in range(0, len(x)):
        if (x[i] < threshold):
            if(x[i] > -threshold):
                x[i] = 0
    return x

def binaryClip(x, threshold = 0.16):
    """
    -----------------------
    An internal clipper function that only keeps the peaks of an incomming signal
    This clipper only returns -1,0 or 1. I call it a binary clipper
    -----------------------
    Variables     :
        x         :  incomming array of audio data
        threshold :  the minumum threshold for a signal to pass through the function
    -----------------------
    Returns       :
        x         :  the clipped data is returned as 1's, -1's or 0's
    -----------------------

    """
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

