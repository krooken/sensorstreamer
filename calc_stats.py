import numpy as np
import matplotlib.mlab as mlab

def ts_means(ts):
    return [np.mean(column) for column in ts['Data'].T]

def ts_vars(ts):
    return [np.var(column) for column in ts['Data'].T]

def ts_std(ts):
    return [np.std(column) for column in ts['Data'].T]

def ts_norm(ts):
    pows = np.power(ts['Data'],2)
    return [np.sqrt(np.add.reduce(pow)) for pow in pows]

def bell_curve(array):
    mean = np.mean(array)
    sigma = np.std(array)

    x = np.linspace(mean - 3.0*sigma, mean + 3.0*sigma)

    curve = mlab.normpdf(x, mean, sigma)

    return x, curve
