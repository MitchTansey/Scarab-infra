#!/bin/bash
set -x #echo on
cd "$(dirname "$0")"

OUTPUT_DIR=/home/$USER/plot/lab3
SIM_PATH=/home/$USER/exp/simulations
DESCRIPTOR_PATH=/home/$USER/lab3.json

mkdir -p $OUTPUT_DIR

python3 plot_ipc.py -o $OUTPUT_DIR -d $DESCRIPTOR_PATH -s $SIM_PATH
