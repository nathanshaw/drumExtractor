# inclass notes on machine learning

theta = np.array([0,0.5])# a guess of theta,

m = len(x)
x = np.vstack((npo.ones(x.shape), x)).T#.T transposes array
# the hyphosis function
def h(x):
#the dot product
    #return theta[0] + theta[1]*x
    return np.dot(theta, x)

def J(theta):
    cost = 0
    for i in range(m):
        cost += (h(x[i]) - y[i])**2
    return cost/(2*m)

def update_theta():
    cd = np.zeros(y.shape)# cd for current difference
    for i in range (m):
        cd[i] = h(x[i]) - y[i]
    new_th0 =  theta[0] - alpha/m * np.sum(cd * x[:,0])
    new_th1 = theta[1] - alpha/m * np.sum(cd * x[:,1])
    theta[0] = aplha/(m * np.sum())
