"""
Different functions for detecting the tempo on incomming audio signals
"""
from rect import fullWave
from onset import envelope
from stft import *
import matplotlib.pyplot as plt

#for convience
def imshow(x, extent=None):
    plt.imshow(x, aspect='auto', interpolation='nearest',origin='lower',extent=extent)

def scheirer(x):
    #divide signal into 6 frequency bins
    freqBins = np.zeros(len(x),6)
    #freqBins = stft(x,len(x)/6, len(x)/6)
    #
    freqBins = envelope(freqBins)
    freqBins = fullWave(freqBins)
    #send derivitive to comb filter bank
    #compare the filter banks

def beatSpectrum(x):
    raise NotImplementedError()
    #stft log magnitudes

    #similarity matrix is created by calculating similarity between each pair of vecors e.g. cosine similarity
    #Beat spectrum is produced by using diagonal sums or autocorrelation to find periodicities in the simularity matrix

def beatHistogram(x):
    raise NotImplementedError()
    #audio is divided into octave sub-bands using DWT
    #Envelopes extracted from each band are re-combined
    #autocorrelation and peak picking is used to find onsets
    #Each onset contribuutes its strength to an overall histogram
