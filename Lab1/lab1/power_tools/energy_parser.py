import sys
import numpy
import itertools

filePtr = open("/tmp/RAPL_Energy_0.txt", "r+")

#line = filePtr.readlines()[1:]

start = numpy.int64(sys.argv[1])
end = numpy.int64(sys.argv[2])

AVE_cpupower = 0.0
i = 0
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


print(" Avg. CPU power : %.4f W\nTotal CPU energy: %.4f J" % (AVE_cpupower/i, total_energy/1000000))

filePtr.close()
