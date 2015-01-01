"""
File containing functions for extracting samples, and naming them
"""
import wave
from scipy.io import wavfile
################

"""
----------------------------------
Proto-functions
----------------------------------
"""

def extractSamples(data, srate, onsets):
    """
    Function for extracting samples from data with a list of onsets
    """
    sampleList = []
    sampNum = 0
    for i in range(len(data)-1):
        if onsets[i] == 1:#if we found a peak
            start = i#set start to that sample
            end = i+(srate)
            found = 0
            #lets find the next onset
            for j in range(i+1, i + srate):#if there is another onset within a third of a second
                if j < len(data)-1:
                    if found == 0:
                        if onsets[j] == 1:
                            end = j + i
                            found = 9
            #load up the sample data into a NP array
            if(end - start > srate//3):
                sampleList.append(data[start:end])
                sampNum = sampNum + 1
    #print('----------------')
    #print(sampleList)
    print('----------------')
    print(sampNum, ' samples extracted')
    print('----------------')
    return sampleList

#def simpleSamples(samples, label=None):


def exportSamples(samples, label=None):
    """
    Function for Exporting Arrays of Audio data as labeled .wav files
    -----------------
    Variables
    -----------------
    samples = incomming array of audio data
    label   = incomming array with labels for incomming audio data
            The function assumes the following :
                0 = data is not percussive, function discards the sample
                1 = data is percussive but of unknown catagory
                2 = data is catagorized as a Kick Drum
                3 = data is catagorized as a Snare
                4 = data is catagorized as a Clap
    -----------------
    Returns :
    -----------------

    -----------------
    """
    tonalCount = 0
    unknownCount = 0
    kickCount = 0
    snareCount = 0
    clapCount = 0
    sampleName = 'unknown00'
    if (label == None):
        print("No label data given, will export all samples with unknown type")
        for i in range(len(samples)):
            sampleName = 'unknown' + str(i) + '.wav'
            print(sampleName)
            createWave(samples[i], sampleName)
        return 0
    else :
        print("Labeling Samples According to Label Data ... ")
        for i in range(len(samples)):
            currentLabel = label[i]
            sampleName, tonalCount, unknownCount, kickCount, snareCount, clapCount = nameMyFile(currentLabel, tonalCount, unknownCount, kickCount, snareCount, clapCount)
            createWave(samples[i], sampleName)
        return 0

def createWave(sample, fileName, srate = 44100):
    wavfile.write(fileName, srate, sample)
    return 0

def createWaveOld(sample, fileName, srate = 44100):
    wavFile = wave.open(fileName, 'wb')
    wavFile.setnchannels(1)
    wavFile.setframerate(srate)
    wavFile.setsampwidth(2*15-1)
    #wavFile.setparams(1, 2, srate, 0, 'NONE', 'not compressed')
    wavFileData = True
    for i in range(len(sample)):
        wavFileData = wavFileData + wave.struct.pack('h', int(sample[i])) #converts to binary
    wavFile.writeframes(wavFileData)
    wavFile.close()

def sampleLength(sample, srate):
    print("Sample length : ", len(sample)/srate, " Seconds")
    return 0

def nameMyFile(labelData, tonalCount, unknownCount, kickCount, snareCount, clapCount):
    if labelData.any() == 0:
        fileName = 'tonal' + str(tonalCount) + '.wav'
        tonalCount = tonalCount + 1
    if (labelData.any()== 1):
        fileName = 'unknown' + str(unknownCount) + '.wav'
        unknownCount = unknownCount + 1
    if (labelData.any() == 2):
        fileName = 'Kick' + str(kickCount) + '.wav'
        kickCount += 1
    if (labelData.any() == 3):
        fileName = 'Snare' + str(snareCount) + '.wav'
        snareCount += 1
    if (labelData.any() == 4):
        fileName = 'Clap' + str(clapCount) + '.wav'

    return fileName, tonalCount, unknownCount, kickCount, snareCount, clapCount

