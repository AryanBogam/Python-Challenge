portfolio = {
    "AAPL": {"qty": 10, "price": 195},
    "TSLA": {"qty": 5, "price": 780},
    "GOOG": {"qty": 2, "price": 2600}
}

# Calculating total portfolio value
total_value = 0
for stock in portfolio:
    qty = portfolio[stock]["qty"]
    price = portfolio[stock]["price"]
    total_value += qty * price

print(f"Total Portfolio Value: ${total_value}")
print("\nRisk Analysis:")

for stock in portfolio:
    qty = portfolio[stock]["qty"]
    price = portfolio[stock]["price"]
    stock_value = qty * price
    
    percentage = (stock_value / total_value) * 100
    
    print(f"{stock}: ${stock_value} ({percentage:.1f}%)", end="")
    
    # Check if it's risky (more than 30%)
    if percentage > 30:
        print(" - HIGH RISK!")
    else:
        print(" - Safe")