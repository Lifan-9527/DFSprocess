#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:37:44 2019

@author: fan

 STFT method:
 The original stft method inside numpy
 seems too complex to use for the DFS
 signal process target. So here is a 
 recomposition of STFT method.
"""
import math
import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import cm
#from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

#_______________________________________________
# Map the simple time-serial sequence into 
# two-dimension space(time-frequency space).
#_______________________________________________
def stft(source, winlen, slide):
    data = source
    # data patch
    topindex = 2**power2Near(len(source))
    if topindex-len(source)>0:
        data = data+[0]*(topindex-len(source))
    # map generation
    winNum = int((len(data)-winlen)/slide)+1
    Map = np.arange(winNum*winlen).reshape(winlen, winNum)
    
    # Insert data into Map
    #for i in range(0,winNum):
    for i in range(0, winNum):
        # winNum-int(winlen/slide)
        # len(data)-winlen
        Map[:,i] = data[slide*i:slide*i+winlen]
    cMap = Map.astype(complex)
    # Map = np.fft.fftshift(Map)
    for i in range(0,winNum):
        cMap[:,i] = np.fft.fft(Map[:,i])    
    return cMap

#_______________________________________________
# compute the nearest power of 2 for input length
#_______________________________________________
def power2Near(k):
    assert(k>0),"Input must be bigger than 0"
    power = 0
    #j = k
    while(True):
        if k>1:
            k=math.ceil(k/2)
            power += 1
        elif k<=1:
            break
    return power
