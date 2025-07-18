q10. Microsoft Account Password Validator
Problem:
You’re building a Microsoft-style password validator for account signup. Write a function that checks if the password meets the following requirements:

At least 8 characters
Contains at least 1 uppercase letter
Contains at least 1 lowercase letter
Contains at least 1 digit
Contains at least 1 special character from !@#$%^&*()_+-=[]{}|;:,.<>?/

If valid, return "Password is strong". Otherwise, return a list of all the rules that were broken.

Example Input:
check_password("Hello123")

Expected Output:
["Must contain a special character"]
