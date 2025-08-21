prices = [400, 1200, 800]

min_price = prices[0]
max_price = prices[0]
total = 0

for price in prices:
    if price < min_price:
        min_price = price
    if price > max_price:
        max_price = price
    total = total + price

avg_price = total / len(prices)

print("Min =", min_price)
print("Max =", max_price)
print("Avg =", avg_price)