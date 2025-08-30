def count_frequency(elements):
    frequency = {}
    for element in elements:
        if element in frequency:
            frequency[element] = frequency[element] + 1
        else:
            frequency[element] = 1
    return frequency

elements = [1, 2, 2, 3, 1, 1]
result = count_frequency(elements)
print(result)