# Function to check if a string is a palindrome
def is_palindrome(text):

    # Convert to lowercase and remove spaces for better comparison
    cleaned_text = text.lower().replace(" ", "")
    
    # Compare string with its reverse
    ans = cleaned_text == cleaned_text[::-1]
    return ans

# Get input from user
user_string = input("Enter a string: ")

# Check if it's a palindrome
result = is_palindrome(user_string)

# Display result
if result:
    print(f"'{user_string}' is a palindrome!")
else:
    print(f"'{user_string}' is not a palindrome.")
