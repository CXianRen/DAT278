#!python3

import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import cpp.build.gemm as clib

def gemm(A, B, C):
    
    assert A.shape[0] == C.shape[0]
    assert A.shape[1] == B.shape[0]
    assert B.shape[1] == C.shape[1]

    return gemm_gpu(A, B, C)

def gemm_py(A, B, C):
      
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i][j] += A[i][k] * B[k][j]

    return C

def gemm_cpp(A, B, C):

     return clib.gemm(A, B, C)
     
def gemm_gpu(A, B, C):

     return clib.gemm_GPU(A, B, C)
