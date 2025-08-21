loads = [40, 30, 60]

min_load = loads[0]
best_gpu_index = 0

for i in range(len(loads)):
    if loads[i] < min_load:
        min_load = loads[i]
        best_gpu_index = i

print("Assign task to GPU", best_gpu_index, "with load", min_load)