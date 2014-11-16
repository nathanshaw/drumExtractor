#!/usr/bin/env python3
"""mfcc.py

Provides mfcc, a Mel-Frequency Cepstral Coefficient function.

Author: [Dexter Shepherd]
Email:  [dexterShepherd@alum.calarts.edu]
Date:   [11/2/14]

CalArts MTEC-480/680
Fall 2014

"""

import numpy as np
from scipy.fftpack import dct
from freqwarp import hz2mel, mel2hz


def mel_filter(fs, fft_size, num_filt=36):
    f = np.arange(fft_size//2+1)*fs/fft_size
    f_edges = mel2hz(np.linspace(hz2mel(f[0]), hz2mel(f[-1]), num_filt+2))

    lo = f_edges[:-2,None]
    hi = f_edges[2:,None]
    w  = np.diff(f_edges)[:,None]

    return 2/(hi-lo) * np.maximum(0, np.minimum(
        (f - lo)/w[:-1], (hi - f)/w[1:]))


def mfcc(X, fs, fft_size=None, num_filt=36):
    """Mel-Frequency Cepstral Coefficients

    Parameters
    ----------
    X : numpy.ndarray
        STFT matrix
    fs : numeric
        Sample rate
    fft_size : int, optional
        Size of FFT that produced X. Default: infer from X.
    num_filt : int, optional
        Number of mel filters to use. Default: 36.

    Returns
    -------
    numpy.ndarray
        2D array of MFCC coefficients for each input column
    """


    if fft_size==None:
       fft_size = (X.shape[0]*2)-1

    mel_warped = np.dot(mel_filter(fs, fft_size, num_filt), np.log(X))
    return dct(mel_warped, type=2, axis=0, norm='ortho')
