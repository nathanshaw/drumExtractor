"""pyConvert.py
------------------
My file for converting wav files into a mono format i can easier work with
------------------
Author      : Nathan Villicana-Shaw
Email       : nathanshaw@alum.calarts.edu
Date        : October 13th, 2014

CalArts MTEC-480
Fall 2014
------------------
"""
import scipy.io.wavfile as wav
import numpy as np

def exportWave(name, srate, data):
    wav.write(name,srate,data)
    return 0

def convert(fname, mode = None):
    """Takes in a wave file, scales it from -1.0 to 1.0
        Converts to mono if not mono
    Parameters
    ---------
    fname : string
        Directory of the wav file
    mode  : if set as 0 the program will take the left channel and throw away the right channel
            if set sd 1 the program will take the arithmetic sum of the two channels and return the normalized signal

    Returns
    -------
    Data  : the actual data

    srate : the sample rate of the given audio file
    -----------
    """
    if mode is None:
        mode = 0
    if (mode > 1):
        mode = 0
    (srate, data) = wav.read(fname)
    data = data.astype('float')/(2**15)
    channels = data.ndim
    print("Your file has ", channels, "Channels")
    if (channels == 1):
        return data, srate
    if (channels > 1 & mode == 0):
        Data = data[:,0]
        print("Throwing away all channels besides the left.")
        return Data, srate
    if (channels > 1 & mode == 1):
        Data = np.zeros(len(data))
        for i in range (0, len(data)):
            total = 0
            for channel in range(0, channels):
                total = total + data[i,channel]
            Data[i] = total/channels
        print("Taking the Mean of all channels and summing to Mono")
        return Data, srate
    else :
        print("Error recognizing file")
        return 0
