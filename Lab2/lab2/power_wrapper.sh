#! /bin/bash

# Run the power measurements in the background
nvidia-smi --query-gpu=timestamp,power.draw --format=csv --loop-ms=5 > power-measurement-gpu.txt  &

# Capture the process ID (PID) of the power measurements
pid=$!

# Run the actual program
"$@"

# Once the actual program has finished
kill $pid

sed -i 's/W//g' ./power-measurement-gpu.txt 