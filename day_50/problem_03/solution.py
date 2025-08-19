prices = [120, 134, 98, 145, 110]

min_price = prices[0]
max_price = prices[0]

for price in prices:
    if price < min_price:
        min_price = price
    if price > max_price:
        max_price = price

print("Min =", min_price, "Max =", max_price)