import itertools

file_ptr = open("/tmp/RAPL_Energy_0.txt", "r+")

avg_cpupower = 0.0
total_cpuenergy = 0.0

i = 0

for line in itertools.islice(file_ptr, 1, None):

    token    = line.strip().split(',')
    energy   = float(token[1])
    cpupower = float(token[2])

    if i == 0:
        energy_old = energy
    if energy >= energy_old:
        total_cpuenergy += energy - energy_old
        avg_cpupower += cpupower
        i += 1
    else:
        total_cpuenergy += energy
    energy_old = energy

print(" Avg. CPU power : %.4f W\nTotal CPU energy: %.4f J" % (avg_cpupower/i, total_cpuenergy/1000000))

file_ptr.close()
