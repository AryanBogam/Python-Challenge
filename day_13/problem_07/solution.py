while True:
    try:
        num = int(input("Enter an integer: "))
        print("Thanks! You entered:", num)
        break
        
    # If input was invalid, show error and try again
    except ValueError:
        print("Invalid input. Try again.")