portfolio = {
    "AAPL": {"qty": 10, "price": 195},
    "TSLA": {"qty": 5, "price": 780},
    "GOOG": {"qty": 2, "price": 2600}
}

total_value = 0

for stock in portfolio:
    qty = portfolio[stock]["qty"]
    price = portfolio[stock]["price"]
    stock_value = qty * price
    
    print(f"{stock}: {qty} shares × ${price} = ${stock_value}")
    total_value += stock_value

print(f"\nTotal Portfolio Value: ${total_value}")