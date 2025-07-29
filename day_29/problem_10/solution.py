nums = [0, 1, 0, 3, 0, 5]

non_zeros = []
zero_count = 0

for num in nums:
    if num != 0:
        non_zeros.append(num)
    else:
        zero_count += 1

result = non_zeros + [0] * zero_count

print(f"Original: {nums}")
print(f"Result: {result}")