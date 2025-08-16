emails = [{"size_kb": 200}, {"size_kb": 300}]

total_size = 0
for email in emails:
    total_size = total_size + email["size_kb"]

print(total_size)