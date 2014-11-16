#!/usr/bin/env python3
"""freqwarp.py

Provides several frequency warping functions.

Author: [Dexter Shepherd]
Email:  [DexterShepherd@alum.CalArts.edu]
Date:   [11/2/14]

CalArts MTEC-480/680
Fall 2014

"""

import numpy as np


def hz2mel(x):
    return 2595*np.log10(1+(x/700))


def mel2hz(x):
    return 7*(10**((x/2595)+2))-700

def hz2bark(x):
    return 26.81*x/(1960 + x) - 0.53

def bark2hz(x):
    return ((196000*x)+103880)/(2628 - (100*x))

def hz2oct(x):
    return np.log2(x/27.5)


def oct2hz(x):
    return 27.5 * 2**x


def hz2midi(x):
    return 21 + 12*np.log2(x/27.5)


def midi2hz(x):
    return 27.5 * 2**((x - 21)/12)


_fns = {'mel':  [ hz2mel,  mel2hz  ],
        'bark': [ hz2bark, bark2hz ],
        'oct':  [ hz2oct,  oct2hz  ],
        'midi': [ hz2midi, midi2hz ] }


def freqwarp(x, units='mel', direction='to'):
    """General frequency warping function

    Parameters
    ----------
    x : numeric or numpy.ndarray
        Input values to warp
    units : string, optional. Default 'mel'.
        Frequency units to warp to/from (other unit is always Hz).
    direction : string, optional. Default 'to'.
        Whether to warp 'to' or 'from' the specified unit.

    Returns
    -------
    Warped frequency value(s).
    """

    if direction == 'to':
        direction = 0
    elif direction == 'from':
        direction = 1

    if units not in _fns.keys() or direction not in [0, 1]:
        raise ValueError('unknown frequency warping requested')

    return _fns[units][direction](x)
