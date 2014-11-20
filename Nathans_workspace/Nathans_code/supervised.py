"""
-----------------------------------
supervised.py
-----------------------------------
code for supervised Machine Learning
-----------------------------------

Author     : Nathan Villican-Shaw
Email      : nathanshawsemail@gmail.com
Date       : November 16th, 2014

CalArts : MTEC-480
Fall 2014
-----------------------------------
-----------------------------------
NOTE    :   This code uses modules from scikit-learn, the code here is basically ab augmented version of the code found on the scikit-learn website
-----------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

"""
Note about the label data :
    0  : not recognized
    1  : Kick Drum
    2  : Snare Drum
    3  : Clap
"""
"""
Note about
"""
"""

"""
#support vector classification for single class
def SVC(data, labels):
    """
    ----------------------------
    Function that implements sklearn's support vector classification supervised machine learning algorithms
    ----------------------------
    Variables :
    ----------------------------
    data      : array of incomming data with features
    labels    : 1d array of label data
    ----------------------------
    Constants :
    ----------------------------
    trainAm   : all datapoints before this number will be used to train program, everything remaining is test data
                This value will be about 76% of the length of the data passed into function
    kernalCo  : the kernal coefficient we will be using, default is rgf
    ----------------------------
    """
    #counters for determining success rate of program farther down line
    right = 0
    wrong = 0
    #the number of samples we will use to train the machine
    trainAm = len(data)//1.3#//1.3 is about 76% of data given
    #the kernal coefficient
    kernalCo = 'rgf'
    clf = svm.SVC()#initalize support vector machine as a classification system
    clf.fit(data[:trainAm], labels[:trainAm])#fits the SVM with data and labels
    # values for the SVM modul of sklearn
    svm.SVC(1.0, kernel=kernalCo, cache_size=400, class_weight=None, coef0=0.0, degree=3, gamma=0.0, max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.0001, verbose=False)
    for i in range(trainAm,len(data)-1,1):
        #the actual predicting
        h = clf.predict(data[i])
        #print the actual predictions vs. results
        print('data ',i,' prediction is :', h)
        print('The label actually is    : ',labels[i])

        #Determines how many are right vs wrong
        if (labels[i] == h):
            right = right + 1
        else:
            wrong = wrong + 1

    #lets print out some info on how well we have done
    print('---------------------------------------------------')
    print('Success rate of : ',right/(right+wrong), 'percent')
    print('Over ',right+wrong,' tested samples')
    print('---------------------------------------------------')
"""
------------------------
Extra Testing Functions :
------------------------
"""
#function for printing data and labels
def printDL():
    print(data)
    print(labels)

#plot the data and labels given
def plotTime():
    plt.plot(data,'b.')
    plt.plot(labels, 'g')
    plt.show()
"""
#load the data up into arrays
data = np.load('data.npy')
labels = np.load('labels.npy')
#Lets do it!!
SVC(data, labels)
"""
