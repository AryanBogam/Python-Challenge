words = ["apple", "banana", "apple", "orange", "banana", "banana"]

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)