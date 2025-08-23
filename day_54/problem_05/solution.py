celsius = [0, 25, 100]

fahrenheit = []
for temp in celsius:
    f = (temp * 9/5) + 32
    fahrenheit.append(int(f))

print(fahrenheit)