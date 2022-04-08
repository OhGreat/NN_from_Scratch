import numpy as np

def mse(y_true, y_pred,ax=0):
    """ Mean squared error
    """
    return ((y_true - y_pred)**2).mean(axis=ax)