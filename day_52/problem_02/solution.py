gpus = [("RTX 3060", 8700), ("RTX 4090", 12500)]

highest_score = 0
best_gpu = ""

for gpu_name, score in gpus:
    if score > highest_score:
        highest_score = score
        best_gpu = gpu_name

print(best_gpu)