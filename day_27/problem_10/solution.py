def apply_discount(price, discount_percent):
    try:
        price = float(price)
        discount_percent = float(discount_percent)
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
        return final_price
    except ValueError:
        return "Invalid input"

print(apply_discount(100, 20))

try:
    price = input("Enter price: ")
    discount = input("Enter discount percent: ")
    result = apply_discount(price, discount)
    print(f"Final price: {result}")
except:
    print("Something went wrong!")