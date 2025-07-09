# Function to count vowels in a string
def count_vowels(text):
    # Define vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Initialize counter
    vowel_count = 0
    
    # Check each character in the string
    for char in text:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Get input from user
user_string = input("Enter a string: ")

# Count vowels and display result
result = count_vowels(user_string)
print(f"The string '{user_string}' contains {result} vowels")