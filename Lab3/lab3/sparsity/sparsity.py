#!python3

import numpy as np
import time

from scipy.sparse import rand
from scipy.sparse import coo_matrix, csc_matrix, csr_matrix

LAYER_SIZES = [
    {'M' :   64, 'N' : 3025, 'K' :  363},
    {'M' :  192, 'N' :  729, 'K' : 1600},
    {'M' :  384, 'N' :  169, 'K' : 1728},
    {'M' :  256, 'N' :  169, 'K' : 3456},
    {'M' :  256, 'N' :  169, 'K' : 2304},
    {'M' : 4096, 'N' :    1, 'K' : 9216},
    {'M' : 4096, 'N' :    1, 'K' : 4096},
    {'M' : 1000, 'N' :    1, 'K' : 4096}]

DENSITIES = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.01]

if __name__ == '__main__':

    # Generate a MxN matrix with density 'd' (in COO format)
    layer = LAYER_SIZES[1]
    M = layer['M']
    N = layer['N']
    K = layer['K']
    d = DENSITIES[1]
    A = rand(M, K, density=d)
    B = rand(K, N, density=d)
    C = rand(M, N, density=d)

    # Convert matrix
    # matrix = matrix.tocsr()
    # matrix = matrix.todense()
    A_d = A.todense()
    B_d = B.todense()
    C_d = C.todense()
    
    start = time.time()

    # Write the code whose power you want to measure here
    for i in range(500):
        C_d = A_d * B_d + C_d

    end = time.time()

    print('  Total time(ms) = ', int(  (end - start) * 1000))
    print('Start Time = ', int(start * 1000))
    print('  End Time = ', int(  end * 1000))
    
