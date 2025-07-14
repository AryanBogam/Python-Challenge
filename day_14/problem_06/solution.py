items = [5, 10, 15, 20]

while True:
    try:
        idx = int(input("Enter an index (0-3): "))
        print(f"Value at index {idx}: {items[idx]}")
        break
    except ValueError:
        print("Please enter a valid number.")  # Not an int
    except IndexError:
        print("Index out of range. Try between 0 and 3.")  # Invalid index
