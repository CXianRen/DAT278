#!/bin/bash

cd src/cpp

# Clean previous build
if [ -d "build" ]; then
  rm -r build
fi

mkdir build
cd build

cmake ..
make