# DAT278 - Sustainable Computing Lab - Lab 2

## Main instructions

Before compiling for CUDA code set the following environment variables;


"vim ~/.bashrc; <br>
export PATH=/chalmers/sw/sup64/cuda_toolkit-12.1.1/bin:$PATH; <br>
export LD_LIBRARY_PATH=/chalmers/sw/sup64/cuda_toolkit-12.1.1/targets/x86_64-linux/lib:$LD_LIBRARY_PATH; <br>
SAVE and QUIT; <br>
source ~/.bashrc"



This lab focuses on offloading the GEMM kernel to a GPU using CUDA programming model. The template for CUDA code is available in the provided lab material. If you don't have experience with CUDA programming language, read this [documentaion](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)

To run the application, use the following command:

`python3 main.py`

In `main.py`, the following variables need to be set:

- `DATASET_PATH` &rarr; path to ImageNet dataset .
- `IMGS_DIR`     &rarr; path to the images from ImageNet (relative to `DATASET_PATH`)
- `LABELS_FILE`  &rarr; path to the labels from ImageNet (relative to `DATASET_PATH`)
- `WEIGHT_FILE`  &rarr; path to the weight file.
- `BATCH_SIZE`   &rarr; number of images to infer.

## Measure power consumption of GPU

Before you start measuring GPU power consumption for the offloaded GEMM kernel, it is essential that you measure idle power consumed by the GPU. To measure this power execute the command `nvidia-smi --query-gpu=timestamp,power.draw --format=csv`. 

The power measurment script is provided for you in `power_wrapper.sh`. To measure the power consumption of GPU, run the command `./power_wrapper.sh python3 ./main.py`. This generates a `power-measurement-gpu.txt` text file with the GPU power consumption every 5 ms. Use this file to calculate average power consumed. 

