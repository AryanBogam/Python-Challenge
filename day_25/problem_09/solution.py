items = ["apple", "banana", "orange", "grape", "mango"]

try:
    index = int(input("Enter index (0-4): "))
    print("Item:", items[index])
except IndexError:
    print("Index too big!")
except ValueError:
    print("Enter a number!")