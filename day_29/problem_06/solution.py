products = ("Laptop", "Phone", "Tablet")

index = int(input("Enter product index: "))

try:
    product = products[index]
    print(f"Product: {product}")
except IndexError:
    print("Product not found!")