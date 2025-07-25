while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Invaild Integer.")
print("Your age is", age)