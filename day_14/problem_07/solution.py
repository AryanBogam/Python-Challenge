try:
    num = input("Enter a number: ")
    try:
        num = float(num)
        result = 100 / num  # Inner try: division
        print("100 divided by your number is:", result)
    except ZeroDivisionError:
        print("You can't divide by zero.")
except ValueError:
    print("That's not a number.")  # Outer try: type conversion
