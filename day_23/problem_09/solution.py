batch1 = {"Aryan": 80, "Riya": 90}
batch2 = {"Riya": 70, "Om": 88}

merged = {}

for name in set(batch1) | set(batch2):
    if name in batch1 and name in batch2:
        merged[name] = (batch1[name] + batch2[name]) / 2
    elif name in batch1:
        merged[name] = batch1[name]
    else:
        merged[name] = batch2[name]

print(merged)