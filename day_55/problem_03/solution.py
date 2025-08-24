def find_armstrong(n):
    armstrong_list = []
    for num in range(n + 1):
        digits = str(num)
        num_digits = len(digits)
        total = 0
        for digit in digits:
            total = total + int(digit) ** num_digits
        if total == num:
            armstrong_list.append(num)
    return armstrong_list

result = find_armstrong(500)
print(result)