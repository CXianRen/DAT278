#include <omp.h>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

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
    
    /***** Write your code here *****/
    #pragma omp parallel for
    for(int i=0; i< a_buf.shape[0]; i++){
        for(int k=0; k < a_buf.shape[1]; k++ )
        {
            for(int j=0; j< b_buf.shape[1]; j++)
            { 
                c_ptr[i*b_buf.shape[1]+j] += a_ptr[i*a_buf.shape[1]+k] * b_ptr[k* b_buf.shape[1]+ j];
            }
        }
    }
    return C;
}

PYBIND11_MODULE(gemm, m) {
    m.def("gemm", &gemm, "Compute C = A * B + C");
}
