import numpy as np
class MinMaxScaler:
    def __init__(self):
        pass
    def fit(self,X):
        self.min = np.min(X)
        self.max = np.max(X)


    def transform(self,X):
        return (X -self.min)/(self.max - self.min)


def cust_scaler(X):
    return (X - np.min(X,axis = 0))/(np.max(X,axis = 0)- (np.min(X,axis = 0)))

def cust_std_scaler(X):
    std1 = np.std(X,axis = 0)   
    return (X -np.mean(X,axis = 0))/std1