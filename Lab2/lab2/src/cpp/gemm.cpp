#include <stdio.h>
#include <stdlib.h>
#include <iostream>

#include <cuda_runtime.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "gemmCuda.cuh"

#define TYPE float

namespace py = pybind11;

// Function to perform C = A * B + C
py::array_t<TYPE> gemm (
    py::array_t<TYPE> A,
    py::array_t<TYPE> B,
    py::array_t<TYPE> C
) {
    
    // Extract data from NumPy arrays
    py::buffer_info a_buf = A.request();
    py::buffer_info b_buf = B.request();
    py::buffer_info c_buf = C.request();

    // Check sizes
    if (a_buf.ndim != 2 || b_buf.ndim != 2 || c_buf.ndim != 2) {
        throw std::runtime_error("Input arrays must be 2D matrices");
    }
    if (a_buf.shape[0] != c_buf.shape[0] || a_buf.shape[1] != b_buf.shape[0] || b_buf.shape[1] != c_buf.shape[1]) {
        throw std::runtime_error("Matrix dimensions are not compatible for multiplication");
    }

    TYPE *a_ptr = static_cast<TYPE *>(a_buf.ptr);
    TYPE *b_ptr = static_cast<TYPE *>(b_buf.ptr);
    TYPE *c_ptr = static_cast<TYPE *>(c_buf.ptr);

    // Compute GEMM
    for (size_t i = 0; i < a_buf.shape[0]; ++i) {
        for (size_t j = 0; j < b_buf.shape[1]; ++j) {
            TYPE sum = c_ptr[i * c_buf.shape[1] + j];
            for (size_t k = 0; k < a_buf.shape[1]; ++k) {
                sum += a_ptr[i * a_buf.shape[1] + k] * b_ptr[k * b_buf.shape[1] + j];
            }
            c_ptr[i * c_buf.shape[1] + j] = sum;
        }
    }

    return C;
}

py::array_t<TYPE> gemm_GPU (
    py::array_t<TYPE> A,
    py::array_t<TYPE> B,
    py::array_t<TYPE> C
) {

     
    
    // Extract data from NumPy arrays
    py::buffer_info a_buf = A.request();
    py::buffer_info b_buf = B.request();
    py::buffer_info c_buf = C.request();

    // Check sizes
    if (a_buf.ndim != 2 || b_buf.ndim != 2 || c_buf.ndim != 2) {
        throw std::runtime_error("Input arrays must be 2D matrices");
    }
    if (a_buf.shape[0] != c_buf.shape[0] || a_buf.shape[1] != b_buf.shape[0] || b_buf.shape[1] != c_buf.shape[1]) {
        throw std::runtime_error("Matrix dimensions are not compatible for multiplication");
    }

    
    TYPE *a_ptr = static_cast<TYPE *>(a_buf.ptr);
    TYPE *b_ptr = static_cast<TYPE *>(b_buf.ptr);
    TYPE *c_ptr = static_cast<TYPE *>(c_buf.ptr);


    // Compute GEMM on GPU

    gemm_cuda(a_ptr, b_ptr, c_ptr, a_buf.shape[0], b_buf.shape[1], a_buf.shape[1]);
    
    return C;

    

}

PYBIND11_MODULE(gemm, m) {
    m.def("gemm", &gemm, "Compute C = A * B + C");
    m.def("gemm_GPU", &gemm_GPU, "Compute C = A * B + C on GPU");
}


