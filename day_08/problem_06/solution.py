# Given in question.
nums = [2, 5, 7, 8, 9, 10]
even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Even: {even}, Odd: {odd}")
