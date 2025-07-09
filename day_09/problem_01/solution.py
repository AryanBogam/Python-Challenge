# Function to create a personalized greeting message.
def greet(name):
    return f"Hello, {name}!"

# Get the user's name from the input.
name = input("Enter name: ").capitalize()

# Display the greeting message.
print(greet(name))