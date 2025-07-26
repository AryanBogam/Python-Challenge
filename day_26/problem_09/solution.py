number = input("Enter a number: ")

total = 0
for digit in number:
    total += int(digit)

print(f"Sum of digits: {total}")