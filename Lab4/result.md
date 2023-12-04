t2:

chenhon@cse-es61-01:~/DAT278/Lab4/code$ bash Freq_List.sh 0
Available Frequencies (KHz) 
3201000 3200000 3000000 2900000 2700000 2500000 2300000 2200000 2000000 1800000 1700000 1500000 1300000 1100000 1000000 800000


t2,2 
```bash
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2000000 0 0 ./AlexNet_Serial 
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 121 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 81 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 154 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   221    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   154    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 18596

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 18602
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701694881389
End    = 1701694882694

 Performance counter stats for 'CPU(s) 0-0':

     2,607,151,374      cpu_core/cycles/                                                   
     8,184,704,013      cpu_core/instructions/                                             
     2,207,466,974      cpu_core/L1-dcache-loads/                                          
       346,888,128      cpu_core/L1-dcache-load-misses/                                    
        16,420,161      cpu_core/LLC-loads/                                                
            61,680      cpu_core/LLC-load-misses/                                          

       1.306538323 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 156 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   377    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701694881389 1701694882694
 Avg. CPU power : 5.6418 W
Total CPU energy: 7.3233 J




```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 3200000 0 0 ./AlexNet_Serial         
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 3200000 
Changing Min Frequency to : 3200000 
Current Frequency  :  
3200000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 123 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 82 tasks into system cpuset...
[==================================================]%
cset: **> 49 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 156 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   221    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   156    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 23966

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 23972
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695051832
End    = 1701695052659

 Performance counter stats for 'CPU(s) 0-0':

     2,641,604,865      cpu_core/cycles/                                                   
     8,183,987,250      cpu_core/instructions/                                             
     2,207,247,141      cpu_core/L1-dcache-loads/                                          
       421,883,566      cpu_core/L1-dcache-load-misses/                                    
        19,500,604      cpu_core/LLC-loads/                                                
            72,347      cpu_core/LLC-load-misses/                                          

       0.827313268 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 158 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   379    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
chenhon@cse-es61-01:/scratch$ 

```
chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695051832 1701695052659
 Avg. CPU power : 11.2267 W
Total CPU energy: 9.2132 J



```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 3000000 0 0 ./AlexNet_Serial  
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 3000000 
Changing Min Frequency to : 3000000 
Current Frequency  :  
3000000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 125 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 82 tasks into system cpuset...
[==================================================]%
cset: **> 49 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 158 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   222    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   158    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 28192

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 28198
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695161176
End    = 1701695162052

 Performance counter stats for 'CPU(s) 0-0':

     2,623,803,548      cpu_core/cycles/                                                   
     8,183,874,048      cpu_core/instructions/                                             
     2,207,225,721      cpu_core/L1-dcache-loads/                                          
       378,927,634      cpu_core/L1-dcache-load-misses/                                    
        17,661,883      cpu_core/LLC-loads/                                                
            57,192      cpu_core/LLC-load-misses/                                          

       0.876567246 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 160 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   382    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand

```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695161176 1701695162052
 Avg. CPU power : 10.3241 W
Total CPU energy: 9.0027 J

```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2900000 0 0 ./AlexNet_Serial   
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2900000 
Changing Min Frequency to : 2900000 
Current Frequency  :  
2900000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 127 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 82 tasks into system cpuset...
[==================================================]%
cset: **> 49 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 160 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   223    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   160    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 30414

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 30420
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695214180
End    = 1701695215085

 Performance counter stats for 'CPU(s) 0-0':

     2,620,444,066      cpu_core/cycles/                                                   
     8,183,865,410      cpu_core/instructions/                                             
     2,207,214,000      cpu_core/L1-dcache-loads/                                          
       376,276,148      cpu_core/L1-dcache-load-misses/                                    
        17,550,364      cpu_core/LLC-loads/                                                
            80,745      cpu_core/LLC-load-misses/                                          

       0.905602333 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 162 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   385    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695214180 1701695215085
 Avg. CPU power : 9.7963 W
Total CPU energy: 8.7922 J


```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2700000 0 0 ./AlexNet_Serial  
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2700000 
Changing Min Frequency to : 2700000 
Current Frequency  :  
2700000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 129 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 79 tasks into system cpuset...
[==================================================]%
cset: **> 47 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 161 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   222    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   161    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 1775

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 1781
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695339408
End    = 1701695340380

 Performance counter stats for 'CPU(s) 0-0':

     2,620,316,494      cpu_core/cycles/                                                   
     8,190,068,849      cpu_core/instructions/                                             
     2,208,939,852      cpu_core/L1-dcache-loads/                                          
       421,278,122      cpu_core/L1-dcache-load-misses/                                    
        19,602,475      cpu_core/LLC-loads/                                                
            65,404      cpu_core/LLC-load-misses/                                          

       0.972639549 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 163 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   385    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695339408 1701695340380
 Avg. CPU power : 9.4518 W
Total CPU energy: 9.1380 J


```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2500000 0 0 ./AlexNet_Serial  
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2500000 
Changing Min Frequency to : 2500000 
Current Frequency  :  
2500000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 131 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 79 tasks into system cpuset...
[==================================================]%
cset: **> 47 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 163 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   221    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   163    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 4900

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 4906
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695425520
End    = 1701695426576

 Performance counter stats for 'CPU(s) 0-0':

     2,636,422,488      cpu_core/cycles/                                                   
     8,193,393,753      cpu_core/instructions/                                             
     2,209,876,680      cpu_core/L1-dcache-loads/                                          
       421,698,320      cpu_core/L1-dcache-load-misses/                                    
        19,612,313      cpu_core/LLC-loads/                                                
            88,337      cpu_core/LLC-load-misses/                                          

       1.056908019 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 165 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   386    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand

```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695425520 1701695426576
 Avg. CPU power : 7.9197 W
Total CPU energy: 8.3363 J


```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 1800000 0 0 ./AlexNet_Serial        
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 1800000 
Changing Min Frequency to : 1800000 
Current Frequency  :  
1800000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 133 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 80 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 165 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   222    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   165    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 7597

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 7720
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695509053
End    = 1701695510516

 Performance counter stats for 'CPU(s) 0-0':

     2,630,004,448      cpu_core/cycles/                                                   
     8,190,277,898      cpu_core/instructions/                                             
     2,209,052,473      cpu_core/L1-dcache-loads/                                          
       405,197,124      cpu_core/L1-dcache-load-misses/                                    
        19,425,647      cpu_core/LLC-loads/                                                
            62,186      cpu_core/LLC-load-misses/                                          

       1.464419050 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 167 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   389    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695509053 1701695510516
 Avg. CPU power : 5.2439 W
Total CPU energy: 7.6338 J


```
henhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 800000 0 0 ./AlexNet_Serial        
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 800000 
Changing Min Frequency to : 800000 
Current Frequency  :  
800000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 135 tasks from root into system cpuset...
[=========henhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 800000 0 0 ./AlexNet_Serial        
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspacehenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 800000 0 0 ./AlexNet_Serial        
Core Shield 0-0
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 0 
ondemand
Changing Scaling Governer for CPU 0 to userspace
New Governer for CPU 0  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 800000 
Changing Min Frequency to : 800000 
Current Frequency  :  
800000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 0-0
cset: --> activating shielding:
cset: moving 135 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 80 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 167 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   167    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 11699

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 11705
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695615279
End    = 1701695617990

 Performance counter stats for 'CPU(s) 0-0':

     2,628,321,014      cpu_core/cycles/                                                   
     8,198,323,009      cpu_core/instructions/                                             
     2,211,398,031      cpu_core/L1-dcache-loads/                                          
       428,699,278      cpu_core/L1-dcache-load-misses/                                    
        19,783,200      cpu_core/LLC-loads/                                                
            84,770      cpu_core/LLC-load-misses/                                          

       2.714729787 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 169 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   389    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemandield for cores 0-0
cset: --> activating shielding:
cset: moving 135 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 80 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(1-23) with 167 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   167    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 11699

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 11705
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695615279
End    = 1701695617990

 Performance counter stats for 'CPU(s) 0-0':

     2,628,321,014      cpu_core/cycles/                                                   
     8,198,323,009      cpu_core/instructions/                                             
     2,211,398,031      cpu_core/L1-dcache-loads/                                          
       428,699,278      cpu_core/L1-dcache-load-misses/                                    
        19,783,200      cpu_core/LLC-loads/                                                
            84,770      cpu_core/LLC-load-misses/                                          

       2.714729787 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 169 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   389    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemandm" cpuset of CPUSPEC(1-23) with 167 tasks running
cset: "user" cpuset of CPUSPEC(0) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user          0 y       0 n     0    0 /user
       system       1-23 y       0 n   167    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 11699

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 11705
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 0 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
Start  = 1701695615279
End    = 1701695617990

 Performance counter stats for 'CPU(s) 0-0':

     2,628,321,014      cpu_core/cycles/                                                   
     8,198,323,009      cpu_core/instructions/                                             
     2,211,398,031      cpu_core/L1-dcache-loads/                                          
       428,699,278      cpu_core/L1-dcache-load-misses/                                    
        19,783,200      cpu_core/LLC-loads/                                                
            84,770      cpu_core/LLC-load-misses/                                          

       2.714729787 seconds time elapsed

Executing application done
Destroying shield for cores 0-0
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 169 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   389    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```
chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695615279 1701695617990
 Avg. CPU power : 3.7342 W
Total CPU energy: 10.0874 J

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695615279 1701695617990
 Avg. CPU power : 3.7342 W
Total CPU energy: 10.0874 J




--------

E


```

chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 3200000 23 23 ./AlexNet_Serial         
Core Shield 23-23
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 23 
ondemand
Changing Scaling Governer for CPU 23 to userspace
New Governer for CPU 23  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 3200000 
Changing Min Frequency to : 3200000 
Current Frequency  :  
3200000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 23-23
cset: --> activating shielding:
cset: moving 137 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 80 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-22) with 169 tasks running
cset: "user" cpuset of CPUSPEC(23) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user         23 y       0 n     0    0 /user
       system       0-22 y       0 n   169    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 16393

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 16400
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
Start  = 1701695749908
End    = 1701695751037

 Performance counter stats for 'CPU(s) 23-23':

     3,606,102,897      cpu_atom/cycles/                                                   
     8,183,745,111      cpu_atom/instructions/                                             
     2,207,373,061      cpu_atom/L1-dcache-loads/                                          
           853,216      cpu_atom/LLC-loads/                                                
            39,619      cpu_atom/LLC-load-misses/                                          

       1.129509942 seconds time elapsed

Executing application done
Destroying shield for cores 23-23
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 171 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   391    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695749908 1701695751037
 Avg. CPU power : 11.9848 W
Total CPU energy: 13.4768 J




```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2900000 23 23 ./AlexNet_Serial        
Core Shield 23-23
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 23 
ondemand
Changing Scaling Governer for CPU 23 to userspace
New Governer for CPU 23  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2900000 
Changing Min Frequency to : 2900000 
Current Frequency  :  
2900000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 23-23
cset: --> activating shielding:
cset: moving 139 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 80 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-22) with 171 tasks running
cset: "user" cpuset of CPUSPEC(23) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user         23 y       0 n     0    0 /user
       system       0-22 y       0 n   171    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 19479

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 19485
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
Start  = 1701695848861
End    = 1701695850104

 Performance counter stats for 'CPU(s) 23-23':

     3,602,220,259      cpu_atom/cycles/                                                   
     8,183,873,774      cpu_atom/instructions/                                             
     2,207,414,323      cpu_atom/L1-dcache-loads/                                          
           897,532      cpu_atom/LLC-loads/                                                
            37,127      cpu_atom/LLC-load-misses/                                          

       1.245015156 seconds time elapsed

Executing application done
Destroying shield for cores 23-23
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 173 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   393    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695848861 1701695850104
 Avg. CPU power : 8.9560 W
Total CPU energy: 11.0071 J



```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2000000 23 23 ./AlexNet_Serial        
Core Shield 23-23
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 23 
ondemand
Changing Scaling Governer for CPU 23 to userspace
New Governer for CPU 23  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 23-23
cset: --> activating shielding:
cset: moving 141 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 80 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-22) with 173 tasks running
cset: "user" cpuset of CPUSPEC(23) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user         23 y       0 n     0    0 /user
       system       0-22 y       0 n   173    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 21688

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 21694
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
Start  = 1701695912293
End    = 1701695914093

 Performance counter stats for 'CPU(s) 23-23':

     3,594,355,537      cpu_atom/cycles/                                                   
     8,184,313,581      cpu_atom/instructions/                                             
     2,207,551,556      cpu_atom/L1-dcache-loads/                                          
           856,884      cpu_atom/LLC-loads/                                                
            21,947      cpu_atom/LLC-load-misses/                                          

       1.801324857 seconds time elapsed

Executing application done
Destroying shield for cores 23-23
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 175 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   395    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand

```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695912293 1701695914093
 Avg. CPU power : 4.8443 W
Total CPU energy: 8.6898 J



```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 1800000 23 23 ./AlexNet_Serial   
Core Shield 23-23
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 23 
ondemand
Changing Scaling Governer for CPU 23 to userspace
New Governer for CPU 23  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 1800000 
Changing Min Frequency to : 1800000 
Current Frequency  :  
1800000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 23-23
cset: --> activating shielding:
cset: moving 143 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 80 tasks into system cpuset...
[==================================================]%
cset: **> 48 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-22) with 175 tasks running
cset: "user" cpuset of CPUSPEC(23) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user         23 y       0 n     0    0 /user
       system       0-22 y       0 n   175    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 24178

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 24184
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
Start  = 1701695980093
End    = 1701695982094

 Performance counter stats for 'CPU(s) 23-23':

     3,596,857,713      cpu_atom/cycles/                                                   
     8,187,483,909      cpu_atom/instructions/                                             
     2,208,443,019      cpu_atom/L1-dcache-loads/                                          
           842,332      cpu_atom/LLC-loads/                                                
            21,279      cpu_atom/LLC-load-misses/                                          

       2.002866218 seconds time elapsed

Executing application done
Destroying shield for cores 23-23
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 177 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   403    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701695980093 1701695982094
 Avg. CPU power : 4.5159 W
Total CPU energy: 9.0075 J


```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 800000 23 23 ./AlexNet_Serial  
Core Shield 23-23
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 23 
ondemand
Changing Scaling Governer for CPU 23 to userspace
New Governer for CPU 23  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 800000 
Changing Min Frequency to : 800000 
Current Frequency  :  
800000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 23-23
cset: --> activating shielding:
cset: moving 145 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 79 tasks into system cpuset...
[==================================================]%
cset: **> 47 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-22) with 177 tasks running
cset: "user" cpuset of CPUSPEC(23) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user         23 y       0 n     0    0 /user
       system       0-22 y       0 n   177    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 27744

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 27750
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
Start  = 1701696075526
End    = 1701696078298

 Performance counter stats for 'CPU(s) 23-23':

     3,598,169,393      cpu_atom/cycles/                                                   
     8,185,718,188      cpu_atom/instructions/                                             
     2,207,958,672      cpu_atom/L1-dcache-loads/                                          
           834,255      cpu_atom/LLC-loads/                                                
            18,377      cpu_atom/LLC-load-misses/                                          

       2.774209434 seconds time elapsed

Executing application done
Destroying shield for cores 23-23
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 179 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   399    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696075526 1701696078298
 Avg. CPU power : 3.3919 W
Total CPU energy: 9.3474 J



```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 3000000 23 23 ./AlexNet_Serial  
Core Shield 23-23
Core Count 1
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 23 
ondemand
Changing Scaling Governer for CPU 23 to userspace
New Governer for CPU 23  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 3000000 
Changing Min Frequency to : 3000000 
Current Frequency  :  
3000000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 23-23
cset: --> activating shielding:
cset: moving 157 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 79 tasks into system cpuset...
[==================================================]%
cset: **> 47 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-22) with 183 tasks running
cset: "user" cpuset of CPUSPEC(23) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   220    2 /
         user         23 y       0 n     0    0 /user
       system       0-22 y       0 n   183    0 /system
Executing application ./AlexNet_Serial      start
Power Monitoring PID : 31736

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 31742
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
WARNING: 23 isn't a 'cpu_core', please use a CPU list in the 'cpu_core' range (0-15)
Start  = 1701696185320
End    = 1701696186523

 Performance counter stats for 'CPU(s) 23-23':

     3,602,267,881      cpu_atom/cycles/                                                   
     8,186,494,230      cpu_atom/instructions/                                             
     2,208,151,711      cpu_atom/L1-dcache-loads/                                          
           901,722      cpu_atom/LLC-loads/                                                
            38,202      cpu_atom/LLC-load-misses/                                          

       1.203527194 seconds time elapsed

Executing application done
Destroying shield for cores 23-23
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 185 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   405    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand


```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696185320 1701696186523
 Avg. CPU power : 10.2660 W
Total CPU energy: 12.3196 J


==========

```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2000000 2 3 ./AlexNet_Parallel      
Core Shield 2-3
Core Count 2
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 2 
ondemand
Changing Scaling Governer for CPU 2 to userspace
New Governer for CPU 2  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 3 
ondemand
Changing Scaling Governer for CPU 3 to userspace
New Governer for CPU 3  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 2-3
cset: --> activating shielding:
cset: moving 155 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 78 tasks into system cpuset...
[==================================================]%
cset: **> 46 tasks are not movable, impossible to movechenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696329698 1701696332051
 Avg. CPU power : 5.5234 W
Total CPU energy: 12.9607 J

         user        2-3 y       0 n     0    0 /user
       system   0-1,4-23 y       0 n   187    0 /system
Executing application ./AlexNet_Parallel      start
Power Monitoring PID : 4659

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packageschenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696329698 1701696332051
 Avg. CPU power : 5.5234 W
Total CPU energy: 12.9607 J



Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 4666
WARNING: 2-3 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-3 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-3 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-3 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-3 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
true
----> OMP_PROC_BIND true
Number of Threads requested = 2
Start  = 1701696329698
End    = 1701696332051chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696329698 1701696332051
 Avg. CPU power : 5.5234 W
Total CPU energy: 12.9607 J


     6,248,666,078      cpu_core/cycles/                                                   
     8,892,569,801      cpu_core/instructions/                                             
     2,212,544,190      cpu_core/L1-dcache-loads/                                          
       218,302,406      cpu_core/L1-dcache-load-misses/                                    
         7,422,648      cpu_core/LLC-loads/                                                
            61,398      cpu_core/LLC-load-misses/                                          

       2.355434407 seconds time elapsed

Executing application done
Destroying shield for cores 2-3
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 189 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   407    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand

```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696329698 1701696332051
 Avg. CPU power : 5.5234 W
Total CPU energy: 12.9607 J

```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2000000 2 5 ./AlexNet_Parallel   
Core Shield 2-5
Core Count 4
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 2 
ondemand
Changing Scaling Governer for CPU 2 to userspace
New Governer for CPU 2  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 3 
ondemand
Changing Scaling Governer for CPU 3 to userspace
New Governer for CPU 3  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 4 
ondemand
Changing Scaling Governer for CPU 4 to userspace
New Governer for CPU 4  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 5 
ondemand
Changing Scaling Governer for CPU 5 to userspace
New Governer for CPU 5  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 2-5
cset: --> activating shielding:
cset: moving 157 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 81 tasks into system cpuset...
[==================================================]%
cset: **> 49 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-1,6-23) with 195 tasks running
cset: "user" cpuset of CPUSPEC(2-5) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   222    2 /
         user        2-5 y       0 n     0    0 /user
       system   0-1,6-23 y       0 n   195    0 /system
Executing application ./AlexNet_Parallel      start
Power Monitoring PID : 7310

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 7338
WARNING: 2-5 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-5 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-5 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-5 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-5 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
true
----> OMP_PROC_BIND true
Number of Threads requested = 4
```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696409602 1701696411753
 Avg. CPU power : 6.1325 W
Total CPU energy: 13.1031 J


```
chenhon@cse-es61-01:/scratch$ bash Freq_Scaling_Chalmers.sh 2000000 2 9 ./AlexNet_Parallel  
Core Shield 2-9
Core Count 8
Frequency Scaling Driver check : 
acpi-cpufreq
Set Governers for all the cores
Existing Frequency Scaling Governer for CPU 2 
ondemand
Changing Scaling Governer for CPU 2 to userspace
New Governer for CPU 2  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 3 
ondemand
Changing Scaling Governer for CPU 3 to userspace
New Governer for CPU 3  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 4 
ondemand
Changing Scaling Governer for CPU 4 to userspace
New Governer for CPU 4  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 5 
ondemand
Changing Scaling Governer for CPU 5 to userspace
New Governer for CPU 5  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 6 
ondemand
Changing Scaling Governer for CPU 6 to userspace
New Governer for CPU 6  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 7 
ondemand
Changing Scaling Governer for CPU 7 to userspace
New Governer for CPU 7  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 8 
ondemand
Changing Scaling Governer for CPU 8 to userspace
New Governer for CPU 8  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Existing Frequency Scaling Governer for CPU 9 
ondemand
Changing Scaling Governer for CPU 9 to userspace
New Governer for CPU 9  
userspace
Max Frequency on this core
3201000
Min Frequency on this core
800000
Changing Max Frequency to : 2000000 
Changing Min Frequency to : 2000000 
Current Frequency  :  
2000000
Done Changing Governers and setting frequencies for all the cores specified by user
Creating shield for cores 2-9
cset: --> activating shielding:
cset: moving 159 tasks from root into system cpuset...
[==================================================]%
cset: kthread shield activated, moving 81 tasks into system cpuset...
[==================================================]%
cset: **> 49 tasks are not movable, impossible to move
cset: "system" cpuset of CPUSPEC(0-1,10-23) with 191 tasks running
cset: "user" cpuset of CPUSPEC(2-9) with 0 tasks running
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   224    2 /
         user        2-9 y       0 n     0    0 /user
       system  0-1,10-23 y       0 n   191    0 /system
Executing application ./AlexNet_Parallel      start
Power Monitoring PID : 10369

RAPL read -- use -s for sysfs, -p for perf_event, -m for msr

Found Unsupported model 151
 Processor type
        0 (0), 1 (0), 2 (0), 3 (0), 4 (0), 5 (0), 6 (0), 7 (0)
        8 (0), 9 (0), 10 (0), 11 (0), 12 (0), 13 (0), 14 (0), 15 (0)
        16 (0), 17 (0), 18 (0), 19 (0), 20 (0), 21 (0), 22 (0), 23 (0)

        Detected 24 cores in 1 packages


Trying sysfs powercap interface to gather results

cset: --> last message, executed args into cpuset "/user", new pid is: 10375
WARNING: 2-9 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-9 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-9 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-9 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
WARNING: 2-9 isn't a 'cpu_atom', please use a CPU list in the 'cpu_atom' range (16-23)
true
----> OMP_PROC_BIND true
Number of Threads requested = 8
Start  = 1701696497463
End    = 1701696499402

 Performance counter stats for 'CPU(s) 2-9':

     8,868,209,395      cpu_core/cycles/                                                   
     9,001,617,369      cpu_core/instructions/                                             
     2,229,144,222      cpu_core/L1-dcache-loads/                                          
       213,786,739      cpu_core/L1-dcache-load-misses/                                    
         7,812,810      cpu_core/LLC-loads/                                                
            60,201      cpu_core/LLC-load-misses/                                          

       1.941825783 seconds time elapsed

Executing application done
Destroying shield for cores 2-9
cset: --> deactivating/reseting shielding
cset: moving 0 tasks from "/user" user set to root set...
cset: moving 193 tasks from "/system" system set to root set...
[==================================================]%
cset: deleting "/user" and "/system" sets
cset: done
cset: 
         Name       CPUs-X    MEMs-X Tasks Subs Path
 ------------ ---------- - ------- - ----- ---- ----------
         root       0-23 y       0 y   417    0 /
Reverting System To Orignal State
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand
Reverting Max Frequency to : 3201000 
Reverting Min Frequency to : 800000 
Changing Scaling Governer to : ondemand

```

chenhon@cse-es61-01:~/DAT278/Lab1/lab1/power_tools$ python3 energy_parser.py 1701696497463 1701696499402
 Avg. CPU power : 6.4605 W
Total CPU energy: 12.4728 J







