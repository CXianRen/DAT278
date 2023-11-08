cmake_minimum_required(VERSION 3.3.2)
project(DAT278)

# Flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -fopenmp")

# Pybind 11
add_subdirectory(../../lib/pybind11 build)
pybind11_add_module(gemm gemm.cpp)