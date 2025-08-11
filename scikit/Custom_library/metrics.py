import numpy as np
def accuracy(X,Y):
    return np.mean(X==Y,axis = 0)

def MSE(X,Y):
    error1 = (X-Y)**2
    mse1 = np.mean(error1)
    return mse1


def mean_absolute_error():
    pass



def mean_abs_percentage_error():
    pass
