# -*- coding: utf-8 -*-
"""
Script to generate MNIST data for training SPN.

"""

import numpy as np
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

def mnist(data_dir, valid=False):
    fd = open(os.path.join(data_dir,'train-images-idx3-ubyte'))
    loaded = np.fromfile(file=fd,dtype=np.uint8)
    trX = loaded[16:].reshape((60000,28*28))
    trX = trX.transpose()

    fd = open(os.path.join(data_dir,'train-labels-idx1-ubyte'))
    loaded = np.fromfile(file=fd,dtype=np.uint8)
    trY = loaded[8:].reshape((60000))

    fd = open(os.path.join(data_dir,'t10k-images-idx3-ubyte'))
    loaded = np.fromfile(file=fd,dtype=np.uint8)
    teX = loaded[16:].reshape((10000,28*28))
    teX = teX.transpose()

    fd = open(os.path.join(data_dir,'t10k-labels-idx1-ubyte'))
    loaded = np.fromfile(file=fd,dtype=np.uint8)
    teY = loaded[8:].reshape((10000))
  
    trY = np.asarray(trY)
    teY = np.asarray(teY)
    

    if valid:
        vaX = trX[:,50000:]
        vaY = trY[50000:]
        trX = trX[:,:50000]
        trY = trY[:50000]
        return trX, teX, trY, teY, vaX,vaY
        
    return trX, teX, trY, teY

if __name__ == "__main__":
    
    datadir = os.path.join(script_dir,'..','..','..','exp','mnist','data')
    try:
        os.makedirs('mnist')
    except:
        pass
    
    trX, teX, trY, teY = mnist(datadir, valid=False)
    np.savetxt('mnist/mnist_test.data',teX, fmt='%d',delimiter='  ')
    np.savetxt('mnist/mnist_train.data',trX, fmt='%d',delimiter='  ')
    print "Done!"