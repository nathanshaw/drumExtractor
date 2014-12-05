"""
File containing functions for extracting samples, and naming them
"""

################

"""
----------------------------------
Proto-functions
----------------------------------
"""

def extractFeatures(sample, srate):
    """
    Function that takes in individual samples and extracts a set of features about that sample

    Returns :
        A list of features, and the sample passed into it
    """

def extractSamples(data, srate, onsets):
    """
    Function for extracting samples from data with a list of onsets
    """
    sampleList = []
    sampNum = 0
    for i in range(len(data)-1):
        if onsets[i] == 1:#if we found a peak
            found = 0
            start = i#set start to that sample
            #lets find the next onset
            for j in range(i+1, i + srate):#if there is another onset within a third of a second
                if j < len(data)-1:
                    if onsets[j] == 1:
                        end = j + i
                        found = 1
            if found == 0:
                end = i+(srate)
            #load up the sample data into a NP array
            sampleList.append(data[start:end])
            sampNum = sampNum + 1
    #print('----------------')
    #print(sampleList)
    print('----------------')
    print(sampNum, ' samples extracted')
    print('----------------')
    return sampleList

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

    if (label == None):
        print("No label data given, will export all samples with unknown type")
        for i in range(len(samples)):
            sampleName = nameFile(1) + str(i)
            #export samples[i]
        return 0

    for i in range(len(samples)):
        sampleName = nameFile(label[i])
        createWave(samples[i], sampleName)
    return 0

def createWave(sample, fileName, srate):
    wavFile = wave.open(fileName, 'w')
    wavFile.setParams((1, 2, srate, 0, 'NONE', 'not compressed'))
    maxVol = 2**15-1.0
    wavFileData = ""
    for i in range(len(sample)):
        wavFileData += pack(sample[i])
    wavFile.writeframes(wavFileData)
    wavFile.writeframes(sample)
    wavFile.close()

def nameFile(label):
    if (label == 0):
        fileName = 'tonal' + str(tonalCount)
        tonalCount += 1
    if (label == 1):
        fileName = 'unknown' + str(unknownCount)
        unknownCount += 1
    if (label == 2):
        fileName = 'Kick' + str(kickCount)
        kickCount += 1
    if (label == 3):
        fileName = 'Snare' + str(snareCount)
        snareCount += 1
    if (label == 4):
        fileName = 'Clap' + str(clapCount)

    return fileName

