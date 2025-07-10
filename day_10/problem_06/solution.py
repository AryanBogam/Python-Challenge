# Find sum of even numbers from 1 to 100
i = 1
total = 0

while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1

# Print result
print("Sum:", total)
