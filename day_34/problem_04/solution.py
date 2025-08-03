holdings = {
    "AAPL": {"qty": 10, "price_yesterday": 190, "price_today": 195},
    "TSLA": {"qty": 5, "price_yesterday": 770, "price_today": 780}
}

total_pnl = 0

print("Daily P&L Report:")

for stock in holdings:
    qty = holdings[stock]["qty"]
    price_yesterday = holdings[stock]["price_yesterday"]
    price_today = holdings[stock]["price_today"]
    
    price_change = price_today - price_yesterday
    
    stock_pnl = qty * price_change
    
    print(f"{stock}: {qty} shares × ${price_change} = ${stock_pnl}")

    total_pnl += stock_pnl

print(f"\nTotal P&L: ${total_pnl}")

if total_pnl > 0:
    print("Profit!")
elif total_pnl < 0:
    print("Loss!")
else:
    print("Break even")