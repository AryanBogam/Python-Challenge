try:
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        raise ValueError("That's not an even number!")
    print("Even number accepted")
except ValueError as e:
    print("Error:", e)
