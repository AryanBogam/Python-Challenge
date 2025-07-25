def check_even(num):
    if num % 2 != 0:
        raise ValueError()

while True:
    try:
        num = int(input("Enter even number: "))
        check_even(num)
        print("Good! That's even.")
        break
    except ValueError:
        print("Try again!")