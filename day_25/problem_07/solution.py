try:
    num1 = float(input("First number: "))
    op = input("Operation (+, -, *, /): ")
    num2 = float(input("Second number: "))
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Bad operation!")
        exit()
    
    print("Result:", result)

except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Enter valid numbers!")
except:
    print("Something went wrong!")