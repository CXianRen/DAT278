# DAT278 - Sustabinable Computing Lab

Lab repository for the course DAT278 Sustainable Computing at Chalmers University of Technology.

## Main instructions

The main part of this lab focuses on optimizing ImageNet inference using AlexNet by improving the performance of matrix-matrix multiplication (GEMM). This is the most time consuming kernel of the application, being the core of multiple layers.

To run the application, use the following command:

`python3 main.py`

In `main.py`, the following variables need to be set:

- `DATASET_PATH` &rarr; path to ImageNet dataset .
- `IMGS_DIR`     &rarr; path to the images from ImageNet (relative to `DATASET_PATH`)
- `LABELS_FILE`  &rarr; path to the labels from ImageNet (relative to `DATASET_PATH`)
- `WEIGHT_FILE`  &rarr; path to the weight file.
- `BATCH_SIZE`   &rarr; number of images to infer.

### Dependencies

PyTorch is required for loading the weights and preprocessing the input images. If it is not installed, you can install it by running:

```
pip3 install torch
pip3 install torchvision
```

## Measure power and energy

### Method 1

To measure power and energy, we can do so by reading the corresponding counters using Intel's RAPL. For that, run `sudo /chalmers/sw/sup64/phc/b/binh/rapl-read` in a terminal, and then launch AlexNet in a second terminal. When AlexNet finishes, go back to the terminal where power was being measured and kill the process with _Ctrl+C_. Then run `power_tools/energy_parser.py` with the start and end times you obtained from running AlexNet, and average power and total energy consumption will be printed.

### Method 2 (if you have your own Linux-based computer)

A simpler method is to measure energy with perf. For that, run `perf stat -e power/energy-core <CMD>`, where `CMD` is the command you want to run (in the case of AlexNet, `python3 main.py`).

If you get an error regarding the _perf\_event\_paranoid_ setting, you can fix it by running `sudo sysctl kernel.perf_event_paranoid=-1`.
