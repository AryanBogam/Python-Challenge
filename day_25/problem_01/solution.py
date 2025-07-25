def safe_divide(a,b):
    return a / b

def main():
    a = int(input("What's a: "))
    b = int(input("What's b: "))
    try:
        print(safe_divide(a,b))
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
main()