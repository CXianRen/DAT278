#include <stdio.h>
#include <stdlib.h>
#include <iostream>

//CUDA RunTime API
#include <cuda_runtime.h>

#include "gemmCuda.cuh"
#define TYPE float
#define BLOCK_SIZE 32


__global__ void gemmCUDA(TYPE* a, TYPE* b, TYPE* c, int n_row, int n_col, int n)
{
    /*Write your gemm kernel here*/
}


void gemm_cuda (TYPE * a_ptr, TYPE * b_ptr, TYPE * c_ptr,int a_row,int b_col, int n)
 {
    
    TYPE *cuda_a, *cuda_b, *cuda_c;

    auto a_mem_size = a_row*n;
    auto b_mem_size = n*b_col;
    auto c_mem_size = a_row*b_col;

    /* Task: Memory Allocation */
    cudaMalloc(&cuda_a, sizeof(TYPE)* a_mem_size);
    cudaMalloc(&cuda_b, sizeof(TYPE)* b_mem_size);
    cudaMalloc(&cuda_c, sizeof(TYPE)* c_mem_size);

    /* Task: CUDA Memory Copy from Host to Device */
    cudaMemcpy(cuda_a, a_ptr, sizeof(TYPE)*a_mem_size, cudaMemcpyHostToDevice);
    cudaMemcpy(cuda_b, b_ptr, sizeof(TYPE)*b_mem_size, cudaMemcpyHostToDevice);
    cudaMemcpy(cuda_c, c_ptr, sizeof(TYPE)*c_mem_size, cudaMemcpyHostToDevice);


    // Compute GEMM

    // change these and check if this works 
    dim3 dimBlock(BLOCK_SIZE,BLOCK_SIZE);
    dim3 dimGrid((b_col+ dimBlock.x - 1) / dimBlock.x, (a_row + dimBlock.y - 1) / dimBlock.y);
    

    gemmCUDA <<<dimGrid, dimBlock>>> (cuda_a, cuda_b,  cuda_c, a_row, b_col, n); 
    

    cudaMemcpy(c_ptr, cuda_c, sizeof(TYPE)*c_mem_size, cudaMemcpyDeviceToHost);

    cudaDeviceSynchronize();

    

    cudaFree(cuda_a);
    cudaFree(cuda_b);
    cudaFree(cuda_c);
    


    
}

