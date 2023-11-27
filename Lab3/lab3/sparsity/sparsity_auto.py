#!python3

import numpy as np
import time

from scipy.sparse import rand
from scipy.sparse import coo_matrix, csc_matrix, csr_matrix

import subprocess

LAYER_SIZES = [
    {'M' :   64, 'N' : 3025, 'K' :  363}, # 1
    {'M' :  192, 'N' :  729, 'K' : 1600}, # 2
    {'M' :  384, 'N' :  169, 'K' : 1728}, # 3
    {'M' :  256, 'N' :  169, 'K' : 3456}, # 4
    {'M' :  256, 'N' :  169, 'K' : 2304}, # 5
    {'M' : 4096, 'N' :    1, 'K' : 9216}, # 6
    {'M' : 4096, 'N' :    1, 'K' : 4096}, # 7
    {'M' : 1000, 'N' :    1, 'K' : 4096}] # 8

DENSITIES = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.01]

if __name__ == '__main__':

    # Generate a MxN matrix with density 'd' (in COO format)
    layer = LAYER_SIZES[0]
    M = layer['M']
    N = layer['N']
    K = layer['K']

    def test(A,B,C,it=100):
        
        start = time.time()
        # Write the code whose power you want to measure here
        for i in range(it):
            C = A @ B + C
        end = time.time()
        return int(start * 1000),int(  end * 1000),int((end - start) * 1000)/it

    def Dense_size(A,B,C):
        return A.data.nbytes + B.data.nbytes+ C.data.nbytes
    
    def COO_size(A,B,C):
        return (A.data.nbytes+B.data.nbytes+C.data.nbytes)+\
                (A.row.nbytes+B.row.nbytes+C.row.nbytes) +\
                (A.col.nbytes+B.col.nbytes+C.col.nbytes)
    
    def CSR_size(A,B,C):
        return (A.data.size+B.data.size+C.data.size)*(8+4) + (A.indptr.size+ B.indptr.size + C.indptr.size)*4 
    print("densities,ds,D_start,D_end,D_dt,COO_s,COO_start,COO_end,COO_dt,CSR_s,CSR_start,CSR_end,CSR_dt")
    for d in DENSITIES:
        A = rand(M, K, density=d)
        B = rand(K, N, density=d)
        C = rand(M, N, density=d)
        coo_s = COO_size(A,B,C)
    
        # Convert matrix
        A_d = A.todense()
        B_d = B.todense()
        C_d = C.todense()
        d_s = Dense_size(A_d,B_d,C_d)
        
        
        A_csr = A.tocsr()
        B_csr = B.tocsr()
        C_csr = C.tocsr()
        csr_s = CSR_size(A_csr,B_csr,C_csr)
        
        it = 50
        # Dense
        time.sleep(1)
        start_d,end_d,time_ms_d = test(A_d,B_d,C_d,it)
        # COO
        time.sleep(1)
        start_coo,end_coo,time_ms_coo = test(A,B,C,it)
        # CSR
        time.sleep(1)
        start_csr,end_csr,time_ms_csr = test(A_csr,B_csr,C_csr,it)
        time.sleep(1)
        print(d,
              d_s,start_d,end_d,time_ms_d,
              coo_s,start_coo,end_coo,time_ms_coo,
              csr_s,start_csr,end_csr,time_ms_csr,sep=',')
    
    