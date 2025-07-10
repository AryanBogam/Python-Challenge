# Function to count even and odd numbers
def count_even_odd(numbers):
    even = sum(1 for n in numbers if n % 2 == 0)
    odd = len(numbers) - even
    return even, odd

# Test the function
nums = [1, 2, 3, 4, 5, 6]
even, odd = count_even_odd(nums)

# Print results
print("Even:", even)
print("Odd:", odd)
