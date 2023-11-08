#!python3

import sys, os
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import cpp.build.gemm as clib

M = 3
N = 5
K = 4

A = np.random.rand(M, K).astype(np.float32)
B = np.random.rand(K, N).astype(np.float32)
C = np.random.rand(M, N).astype(np.float32)

C_validation = np.copy(C)

C = clib.gemm(A, B, C)

C_validation = (A @ B) + C_validation

print(np.allclose(C, C_validation))