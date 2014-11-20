"""
fftPlot.py
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import hann

figsize = (12,4)

def peakPlot(x, p, srate=None):
    """

    """
    if(srate == None):
        srate = 44100
        print("No sample rate passed to plotter assuming 44100")
    time = len(x)/srate
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, xlim=(0,0.15),ylim=(-0.3,0.3))
    print("time :",time)
    print("x :",x)
    print("peaks are 1 : ", p)
    ax.plot(time, np.real(np.abs(x)))
    ax.plot(t[p], data[p], 'r.')
    plt.show()


def fftPlt (X, srate=None):
    """Takes untreated  FFT data and shapes it for visual display
    -----------------------
    Variables:
    X = incomming np array of FFT data scaled from -1 to 1
    ----------------------------
    Returns:

    none : just plots the info
    ----------------------------
    """
    #figsize(20,6)
    plt.imshow(10*np.log10(np.real(np.abs(X)+.000001)),origin='lower', interpolation='nearest', aspect='auto')
    plt.ylabel("Frequency")
    plt.xlabel("Time")
    plt.colorbar()
    plt.title("FFT plot")
    plt.show()
    return 0


def plainPlt(X, mode=None):

    if (mode == None):
        mode = 2
    if (mode == 1):
        plt.plot(np.real(np.abs(X)))
    if (mode==2):
        plt.plot(np.real(X))
    plt.autoscale(tight=True)
    plt.show()

    return 0


def pPlt(X, mode=None, x1=None, x2=None, y1=None, y2=None,srate=None):

    if (mode == None):
        mode = 2
    if (mode == 1):
        plt.plot(np.real(np.abs(X)))
    if (mode==2):
        plt.plot(np.real(X))
    if (srate ==  None):
        srate = 44100
    figsize = (12,4)
    seconds = (len(X)/srate)
    time  = np.linspace(0, seconds, num=len(X))
    plt.plot(time,X)
    plt.title("Sample's Waveform")
    plt.autoscale(tight=True)
    plt.ylabel('Amplitude')
    plt.xlabel('Seconds')
    plt.axis([x1,x2,y1,y2])
    plt.show()

    return 0
def stftPlt(X):
    # discard frequencies above Nyquist
    X = X[:len(X)//2+1]
    # take magnitudes and convert to dB
    Xdb = 20*np.log10(np.abs(X))
    # plot
    plt.imshow(Xdb, origin='lower', interpolation='nearest', aspect='auto')
    plt.colorbar()
    return 0

def timePlt (X,x1=None, x2=None, y1=None, y2=None,srate=None):
    """ this is a plotter for the time domain
    ----------------
    Variables:

    X = incomming array of amplitude data

    srate = the sample rate from the data being alalysed, for accurate time

    ----------------
    Returns :

    none, it just plots the data
    ----------------
    """
    if (srate ==  None):
        srate = 44100
    figsize = (12,4)
    seconds = (len(X)/srate)
    time  = np.linspace(0, seconds, num=len(X))
    plt.plot(time,X)
    plt.title("Sample's Waveform")
    plt.autoscale(tight=True)
    plt.ylabel('Amplitude')
    plt.xlabel('Seconds')
    plt.axis([x1,x2,y1,y2])
    plt.show()
    return 0
