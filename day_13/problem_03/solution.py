try:
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        print("Not even!")
    else:
        print("Even number")

# Handle when user enters invalid input (like letters or decimals)
except ValueError:
    print("Please enter an integer.")