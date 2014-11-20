"""
------------------------------
Machine Learning code
------------------------------
Author    :  Nathan Villicana-Shaw
email     :  nathanshawsemail@gmail.com
date      :  November 17, 2014

CalArts : MTEC 480
Fall 2014
------------------------------

NOTE :  requires psikit-learn to operate
NOTE :  linearRegression code is from Chad Wagner
NOTE :  DBSCAN code is augmented code from psikit-learn DBSCAN DEMO code modified to work for sample data, the plotting is pulled directly from the DEMO code

------------------------------
------------------------------

"""

#import sklearn.cluster.KMeans as kmeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN

#these next three functions are pulled from Chad Wagners inclass lecture notes in ipthon notebook
#define hypthesis (h)
#h is a function of input features x but is evaluated on model parameter theta
def h(x, theta):
    return theta[0] + theta[1]*x

#define function for cost or J
#J is a function of model parameters theta, but evaluated on training dataset
def J (theta, x, y):
    return 0.5*np.mean((h(x, theta) - y)**2)

#define function for taking one gradient descent step
#takes current theta and returns new theta
#also depends on training dataset and learning rate alpha
def gd_step(theta, x, y, alpha):
    cd = h(x, theta) - y#current difference, needed twice, calculated once
    return theta - alpha * np.array([np.mean(cd), np.mean(cd*x)])

#this is the code from the ipython notebook, i was using it for a better understanding
def linearRegression(x, y):
    # Constants
    thresh = 1e-10#inter-step cost difference threshold for convergance
    alpha = 0.01#learning rate of program

    #Variables :
    theta = np.array([1.,1.])#inital theta any random values should work
    c0 = J(theta, x, y)#initial cost
    #loop :
    while True:
        #performs the gradient sescent step
        theta = gd_step(theta, x, y, alpha)
        #test for convergance
        c1 = J(theta, x, y)
        if c0 - c1 < thresh:
            break
        c0 = c1
    print('theta : ', theta)
    print('cost : ', c1)
    plt.plot(x,y,'b.')
    plt.plot([0.,16.], h(np.array([0.,16.]), theta), 'r')
    plt.show()

def kMeansDBScan(X, eps=0.3, minSamples=10,):
    """
    ------------------------------
    DBSCAN : views clusters as areas of high density surrounded by areas of low density

    code is modified version of example code given on scikit-learn website, thank you scikit-learn website
    Constants/Variables of interest :
    ------------------------------
    min_samples    : higher value necessary to form a cluster
    eps            : lower value necessary to form a cluster
    ----
    a sample is defined as a core sample that there exists min_samples other samples within a distance of eps
    ------------------------------
    Returns   :
    ------------------------------
    Noting but it prints out data and clusters
    ------------------------------
    """
    db = DBSCAN(eps=eps, min_samples=minSamples).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    #number of clusters in labels
    nClusters = len(set(labels)) - (1 if -1 in labels else 0)
    print('Estimated number of clusters: %d' % nClusters)

    # Plot result
    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
        # Black used for noise.
            col = 'k'
        class_member_mask = (labels == k)
        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=14)

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)

    plt.title('Estimated number of clusters: %d' % nClusters)
    plt.show()
"""
The actual program
"""
#load the data into np arrays and plot
x = np.load('data.npy')
kMeansDBScan(x,1.23,13)
