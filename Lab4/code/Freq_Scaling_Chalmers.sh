
#!/bin/bash

freq=$1
CORE_SHIELD_START=$2
CORE_SHIELD_END=$3
EXECUTABLE="$4 $5 $6 $7 $8 $9"

CPU_FREQ="/chalmers/sw/sup64/phc/b/binh/cpufreq-conf"

CSET=/usr/bin/cset

RAPL_READ=/chalmers/sw/sup64/phc/b/binh/rapl-read

CORE_SHIELD=${CORE_SHIELD_START}-${CORE_SHIELD_END}

echo "Core Shield" $CORE_SHIELD

noThread=$((CORE_SHIELD_END - CORE_SHIELD_START + 1 ))

echo "Core Count" $noThread

thread_count=$noThread

export thread_count
export OMP_NUM_THREADS=$noThread

echo "Frequency Scaling Driver check : "
CUR_SCALING_DRIVER=$(sudo ${CPU_FREQ} read 0 scaling_driver)
echo $CUR_SCALING_DRIVER


if [ $CUR_SCALING_DRIVER != "acpi-cpufreq" ]
then
    echo "ERROR: Please Change the driver to acpi-cpufreq! "
  	echo "INTEL pstate doesnot allow frequency switching"
  	return
fi

echo "Set Governers for all the cores"

for ((cp = CORE_SHIELD_START; cp <= CORE_SHIELD_END; cp++))
do
	#echo "CP ${cp}"
	echo "Existing Frequency Scaling Governer for CPU ${cp} "

	sudo ${CPU_FREQ} read ${cp} scaling_governor
	echo "Changing Scaling Governer for CPU ${cp} to userspace"
	sudo ${CPU_FREQ} set ${cp} scaling_governor userspace
	echo "New Governer for CPU ${cp}  "
	sudo ${CPU_FREQ} read ${cp} scaling_governor

	sleep 1

	echo "Max Frequency on this core"
	sudo ${CPU_FREQ} read ${cp} cpuinfo_max_freq

	echo "Min Frequency on this core"
	sudo ${CPU_FREQ} read ${cp} cpuinfo_min_freq

	echo "Changing Max Frequency to : $freq "
	sudo ${CPU_FREQ} set ${cp} scaling_max_freq $freq

	echo "Changing Min Frequency to : $freq "
	sudo ${CPU_FREQ} set ${cp} scaling_min_freq $freq

	echo "Current Frequency  :  "
	sudo ${CPU_FREQ} read ${cp} cpuinfo_cur_freq

	sleep 1

done

echo "Done Changing Governers and setting frequencies for all the cores specified by user"

echo "Creating shield for cores $CORE_SHIELD"
sudo ${CSET} shield --cpu  $CORE_SHIELD --kthread on
sudo ${CSET} set

#  cycles,instructions,l2_request.all,l2_request.miss

echo "Executing application $EXECUTABLE start"

# Run the power measurements in the background
sudo  ${RAPL_READ} &
pid_rapl=$!
echo "Power Monitoring PID : $pid_rapl"

sleep 1

sudo ${CSET} shield --exec  perf stat -- -C $CORE_SHIELD -e cycles,instructions,L1-dcache-loads,L1-dcache-load-misses,LLC-loads,LLC-load-misses $EXECUTABLE

echo "Executing application done"

kill $pid_rapl

echo "Destroying shield for cores $CORE_SHIELD"
sudo ${CSET} shield --reset
sudo ${CSET} set


echo "Reverting System To Orignal State"

for ((cp = CORE_SHIELD_START; cp <= CORE_SHIELD_END; cp++))
do
	MAX_FREQ=$(sudo ${CPU_FREQ} read ${cp} cpuinfo_max_freq)
	echo "Reverting Max Frequency to : $MAX_FREQ "
	sudo ${CPU_FREQ} set ${cp} scaling_max_freq $MAX_FREQ

	MIN_FREQ=$(cat /sys/devices/system/cpu/cpu${cp}/cpufreq/cpuinfo_min_freq)
	echo "Reverting Min Frequency to : $MIN_FREQ "
	sudo ${CPU_FREQ} set ${cp} scaling_min_freq $MIN_FREQ

	# Revert Governer to ondemand after experiment
	echo "Changing Scaling Governer to : ondemand"
	sudo ${CPU_FREQ} set ${cp} scaling_governor ondemand

	sleep 1

done





