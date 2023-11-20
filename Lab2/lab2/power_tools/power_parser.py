import itertools

file_ptr = open("../power-measurement-gpu.txt", "r+")

avg_gpupower = 0.0
total_gpuenergy = 0.0

i = 0

for line in itertools.islice(file_ptr, 2, None):

    token    = line.strip().split(',')
    gpupower = float(token[1])

    avg_gpupower += gpupower
    i += 1
    

print("Avg. gpu power: %.4f\n" % (avg_gpupower/i))

file_ptr.close()
