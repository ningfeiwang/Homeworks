
from sklearn.linear_model import LinearRegression as LR
import numpy as NP


def impute(X):
    ''' 
    impute missing values in lass column of X using linear regression
    input: X matrix with missing values
    output: modified X with mising values imputed
    '''
    [n, m] = X.shape
    missing_idx = NP.squeeze(NP.isnan(X[:, m-1]))
    complete_idx = NP.logical_not(missing_idx)
    Y = X[complete_idx, :]
    lr = LR()
    lr.fit(Y[:,:m-1], Y[:,m-1])
    Y = X[missing_idx, :]    
    X[missing_idx, m-1] = NP.squeeze(lr.predict(Y[:,:m-1]))

    return X
    

if __name__ == '__main__':

    # simple test code    
    X = NP.array([[1, 2, 3], [2, 4, NP.nan], [3, 6, 9]])
    print 'Before:\n', X
    print 'After:\n', impute(X)

    
