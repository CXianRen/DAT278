#!/bin/bash


Core=$1

if [ -z "$Core" ]
then
    echo "ERROR: Please specify a core number"
  	return
fi

FREQ_LIST="/sys/devices/system/cpu/cpu${Core}/cpufreq/scaling_available_frequencies"
echo "Available Frequencies (KHz) "
CUR_FREQ_LIST=$(cat $FREQ_LIST | cut -d " " -f 1-17)
echo ${CUR_FREQ_LIST}



