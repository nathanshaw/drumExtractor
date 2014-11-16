import matplotlib.pyplot as plt
import numpy as np
from mfcc import mfcc 
from read import read
from stft import stft

fname = "sineSweep.wav"
(srate, data) = read(fname, "mono")
N = 1024
X= stft(data, N)
X = np.abs(X)
X = X[:N/2+1]
X = mfcc(X, 44100)
#mag to dec conversion
#X = 10 * np.log10(X)
plt.imshow(X[1:], interpolation='nearest', aspect='auto', origin='lower')
plt.show()
