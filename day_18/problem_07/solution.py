store = {
    "Office 365": 4999,
    "Windows 11 Pro": 13499,
    "Xbox Game Pass": 699
}

cart = []

def add_to_cart(item):
    if item in store:
        cart.append(item)

def remove_from_cart(item):
    if item in cart:
        cart.remove(item)

def total_cart():
    return sum(store[item] for item in cart)

add_to_cart("Office 365")
add_to_cart("Xbox Game Pass")
print("Total:", total_cart())
