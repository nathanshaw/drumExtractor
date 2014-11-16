import matplotlib.pyplot as plt
import numpy as np
from stft import stft
from read import read

fname = "sineSweep.wav"
(srate, data) = read(fname, "mono")
N = 1024
X= stft(data, N)

X = np.abs(X)
#mag to dec conversion
X = 20*np.log10(X)
plt.imshow(X[:N/2, :], interpolation='nearest', aspect='auto', origin='lower')
plt.show()
