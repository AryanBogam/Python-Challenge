price = float(input("Enter product price: ₹"))
is_prime = input("Are you a Prime member? (yes/no): ").lower()

if is_prime == "yes":
    price *= 0.9

print(f"Final Price: ₹{price:.2f}")