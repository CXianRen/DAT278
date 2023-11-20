cmake_minimum_required(VERSION 3.3.2)
project(DAT278 LANGUAGES CXX CUDA)

set(CMAKE_CUDA_STANDARD 11)

find_package(CUDA  REQUIRED)
include_directories("${CUDA_INCLUDE_DIRS}")

# Flags

# Pybind 11
add_subdirectory(../../lib/pybind11 build)


add_library(gemmcuda STATIC
    gemmCuda.cu
)

set_target_properties(gemmcuda PROPERTIES 
    POSITION_INDEPENDENT_CODE ON
    CUDA_VISIBILITY_PRESET "hidden"
   #CUDA_SEPARABLE_COMPILATION ON
)

add_library(gemm MODULE
    gemm.cpp
)

set_target_properties(gemm PROPERTIES 
    CXX_VISIBILITY_PRESET "hidden"
    INTERPROCEDURAL_OPTIMIZATION TRUE
    PREFIX "${PYTHON_MODULE_PREFIX}"
    SUFFIX "${PYTHON_MODULE_EXTENSION}"
)


target_link_libraries(gemm PRIVATE gemmcuda)
target_link_libraries(gemm PRIVATE pybind11::module)

#

#pybind11_add_module(gemm gemm.cpp )
