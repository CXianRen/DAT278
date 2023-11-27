import sys
import numpy
import itertools

import pandas

csv = pandas.read_csv("./../sparsity/layer1.txt")
def check(start,end):
    filePtr = open("/tmp/RAPL_Energy_0.txt", "r+")
    i = 0
    AVE_cpupower = 0.0
    total_energy = 0.0
    for line in itertools.islice(filePtr, 1, None):
        token    = line.strip().split(',')
        time     = numpy.int64(token[0])
        energy   = float(token[1])
        cpupower = float(token[2])

        if time >= start and time <= end:
            if i == 0:
                energy_old = energy
            if energy >= energy_old:
                total_energy += energy - energy_old
                AVE_cpupower += cpupower
                i += 1
            else:
                total_energy += energy
            energy_old = energy
        elif time > end:
            break
        else:
            continue
    filePtr.close()
    
    return (AVE_cpupower/i), (total_energy/1000000)
    #print(" Avg. CPU power : %.4f W\nTotal CPU energy: %.4f J" % (AVE_cpupower/i, total_energy/1000000))


for i in range(10):
    print("f,", csv.iloc[i][0], end=",")
    # dense
    start = csv.iloc[i][2]
    end = csv.iloc[i][3]
    # print(start, end)
    p,e = check(start,end)
    print(p,e,sep=',', end=",")
    # coo
    start = csv.iloc[i][6]
    end = csv.iloc[i][7]
    # print(start, end) 
    p,e = check(start,end)
    print(p,e,sep=',', end=",")
    # CSR
    start = csv.iloc[i][10]
    end = csv.iloc[i][11]
    # print(start, end)
    p,e = check(start,end)
    print(p,e,sep=',')