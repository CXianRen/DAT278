#include <stdio.h>
#include <stdlib.h>

//CUDA RunTime API
#include <cuda_runtime.h>

#define TYPE float


__global__  void gemmCUDA(const TYPE* a, const TYPE* b, TYPE* c, int n_row, int n_col, int n) ;

void gemm_cuda (TYPE * a_ptr, TYPE * b_ptr, TYPE * c_ptr,int a_row,int b_col, int n);

