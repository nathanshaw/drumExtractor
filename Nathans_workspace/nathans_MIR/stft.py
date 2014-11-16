"""
stft.py
"""
"""
My file for providing stft: Short-Form Transform function : a type of FFT analysis

Author : Nathan Villicana-Shaw
Email : nathanshaw@alum.calarts.edu
Date : Sep 22, 2014

Calarts : MTEC-480
Fall 2014


"""
import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft
#from fftPlot import fftPlt

def stft(x, N=None, hop=None, win=None):
    """
    Give stft analysis of data
    ------------------------
    Variables :
    ------------------------
    x   = the imput data, a np.array of amplitude data ranging from -1 to 1
    N   = the number of samples in each window
        default value = 256
    hop = The distance between the windows
        Default value = N//2
    win = how the data is alaysed,
        Default value is 'hann'
    ------------------------
    Returns

    X = fft data
    _________________________
    """
    #print("This is the incomming data x:", x)
    if N is None:#number of samples in each window
        N = 2**11#2048
    if hop is None: #this is the distance between FFT windows(by default we have it as 1/2 the window size
        hop = N//3
    if win is None:
        win = 'hann'

    window = get_window(win, N)
    xLen = len(x)
    #print("the shape of x : ",x)
    X = np.empty((xLen//hop, N), dtype=np.complex)#create an array to dump data into
    #print("number of data points :", xLen)
    for i in range(0,xLen - N, hop):

        chunk = window*x[i:i+N]
        myFFT = fft(chunk)
        X[i//hop,:] = myFFT

    X = X[:,:N//2 +1]
    X = X.transpose()

    return X





