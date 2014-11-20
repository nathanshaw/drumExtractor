#functions for extracting features from audio signals
from scipy import *
import numpy as np

def hfc(x):


def flatness(x):
    256, 128, 64, 32, 16, 8, 4, 2
    X1 = x[:128,:]
    X2 = x[128:256,:]
    X3 = x[256:,:]

    K1 = X1.shape[0]
    GeoMean = np.prod(np.abs(X1), axis=0)**(1/K1)
    arithMean = np.sum(np.abs(X1), axis=0)/K1

    flat1 = geoMean/arithMean#the flatness for the first bin
