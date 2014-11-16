#!/usr/bin/env python3
"""stft.py

Provides stft, a Short-Time Fourier Transform function.

Author: Dexter Shepherd
Email:  DexterShepherd@alum.calarts.edu
Date:   9/20/14

CalArts MTEC-480/680
Fall 2014

"""

import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft



def stft(x, N=None, hop=None, win=None):
    """Short-time Fourier transform

    Parameters
    ----------
    x : numpy.ndarray
        Vector of samples to analyze (1 channel)
    N : int, optional
        Window size for each FFT. Default 1024.
    hop : int, optional
        Hop size between successive windows. Default N//2.
    win : string, float, or tuple, optional
        Window type and/or parameters (c.f. scipy.signal.get_window)
        Default 'hann'.

    Returns
    -------
    numpy.ndarray
        2D array of complex spectral values over time
    """

    # Set default values in event they are not specified
    if N is None:
        N = 1024
    if hop is None:
        hop = N//2
    if win is None:
        win = "hann"

    #get window array with size of N
    win = get_window(win, N)

    #calculate the number of FFT calcluations we can fit into out for loop and create an empty array to store them in
    numFFTs = (len(x)//hop)+1
    X = np.zeros((N, numFFTs))

    counter = 0

    #iterate through sample in hops
    for i in range(0, len(x), hop):
        #take N sized chunks of our input sample
        choppedSamples = x[i:i+N]
        #if we have fewer samples left than N
        if choppedSamples.shape[0] < N:
            #add the appropriate amount of zeros the windowing function doesn't freak out
            zeroPad = np.zeros(N-choppedSamples.shape[0])
            choppedSamples = np.hstack((choppedSamples, zeroPad))
            #multiply our input array with our window array
        choppedSamples = win*choppedSamples
        #take the FFT of our windowed input, store in our output matrix and return
        X[:, counter] = fft(choppedSamples, N)
        counter += 1
    return X

