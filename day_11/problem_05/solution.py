
data = [("Aryan", 90), ("Elon", 99), ("Zuck", 85)]

# Sort by second item in tuple, reverse = True for descending
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

print(sorted_data)

