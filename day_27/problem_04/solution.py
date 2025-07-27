def is_even(number):
    try:
        num = int(number)
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except ValueError:
        return "Invalid input"

print(is_even(4))
print(is_even("four"))