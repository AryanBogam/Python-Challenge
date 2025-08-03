positions = {
    "AAPL": 100,
    "TSLA": -50,
    "NFLX": 0,
    "GOOG": 20
}

print("Position Analysis:")

for stock in positions:
    qty = positions[stock]
    
    if qty > 0:
        position_type = "LONG"
    elif qty < 0:
        position_type = "SHORT"
    else:
        position_type = "NEUTRAL"
    
    print(f"{stock}: {qty} shares - {position_type}")