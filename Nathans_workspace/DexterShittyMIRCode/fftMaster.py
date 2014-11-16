import matplotlib.pyplot as plt
import numpy as np
from stft import stft
from read import read


fname = "doubleBass.wav"

(srate, data) = read(fname, "mono")
N = 1024
hop = N//2
win = "hann"
X= stft(data, N, hop, win)

X = np.abs(X)
#mag to dec conversion
X = 20*np.log10(X)
plt.imshow(X[:N/2, :], interpolation='nearest', aspect='auto', origin='lower')
plt.colorbar()
plt.title(str(fname) + ", N = " + str(N) + ", hop = N//2,  win = hann")
plt.show()

