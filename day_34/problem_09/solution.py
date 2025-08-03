portfolio = {
    "AAPL": {"qty": 10, "price": 195, "sector": "Tech"},
    "JNJ": {"qty": 5, "price": 170, "sector": "Healthcare"},
    "TSLA": {"qty": 5, "price": 780, "sector": "Auto"}
}

total_value = 0
for stock in portfolio:
    qty = portfolio[stock]["qty"]
    price = portfolio[stock]["price"]
    total_value += qty * price

print(f"Total Portfolio Value: ${total_value:,}")

sector_values = {}

for stock in portfolio:
    qty = portfolio[stock]["qty"]
    price = portfolio[stock]["price"]
    sector = portfolio[stock]["sector"]
    stock_value = qty * price

    if sector in sector_values:
        sector_values[sector] += stock_value
    else:
        sector_values[sector] = stock_value

print("\nSector Breakdown:")

for sector in sector_values:
    value = sector_values[sector]
    percentage = (value / total_value) * 100
    
    print(f"{sector}: ${value:,} ({percentage:.1f}%)")

print("\nStock Details:")
for stock in portfolio:
    qty = portfolio[stock]["qty"]
    price = portfolio[stock]["price"]
    sector = portfolio[stock]["sector"]
    stock_value = qty * price
    
    print(f"{stock} ({sector}): {qty} shares × ${price} = ${stock_value:,}")