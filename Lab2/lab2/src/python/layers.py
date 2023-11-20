#!python3

import numpy as np
import math

from gemm import gemm
from im2col import im2col

def AdaptiveAvgPool2d(ifmap, rows_out, cols_out):

    channels = ifmap.shape[0]

    # Squared ifmaps
    rows = cols = int(math.sqrt(ifmap.shape[1]))

    stride = rows // rows_out  
    pool   = rows - (rows_out - 1) * stride 

    ofmap = np.zeros((channels, rows_out * cols_out)).astype(np.float32)

    for c in range(channels):
        for i in range(rows_out):
            i_s = i * stride
            for j in range(cols_out):
                j_s = j * stride
                acc = 0
                for ii in range(pool):
                    for jj in range(pool):
                        acc += ifmap[c, (i_s+ii)*cols+(j_s+jj)]
                ofmap[c, i * cols_out + j] = acc / (pool * pool)

    return ofmap

def Conv2d(ifmap, weights, bias, ksize, stride, pad):

    ifmap = im2col(ifmap, ksize, stride, pad)

    ofmap_t = np.tile(bias, (ifmap.shape[1],1)).T
    ofmap_t = np.ascontiguousarray(ofmap_t) # Enforce row_major format

    return gemm(weights, ifmap, ofmap_t)

def Linear(ifmap, weights, bias):

    return gemm(weights, ifmap, bias)

def MaxPool2d(ifmap, pool, stride):

    channels = ifmap.shape[0]

    # Squared ifmaps
    rows = cols = int(math.sqrt(ifmap.shape[1]))

    rows_out = ((rows - pool) // stride) + 1
    cols_out = ((cols - pool) // stride) + 1

    ofmap = np.zeros((channels, rows_out * cols_out)).astype(np.float32)

    for c in range(channels):
        for i in range(rows_out):
            i_s = i * stride
            for j in range(cols_out):
                j_s = j * stride
                max_val = float('-inf') # Start from the lowest possible value
                for ii in range(pool):
                    for jj in range(pool):
                        max_val = max(ifmap[c, (i_s+ii)*cols+(j_s+jj)], max_val)
                ofmap[c, i * cols_out + j] = max_val

    return ofmap

def ReLU(ifmap):

    return np.maximum(ifmap, 0)