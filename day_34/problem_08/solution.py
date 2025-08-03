prices = [100, 102, 103, 105, 104, 103, 102, 101]

print("Price History:", prices)
print("\nDaily Signals:")

for i in range(len(prices)):
    print(f"Day {i+1}: ${prices[i]}", end="")

    if i < 2:
        print(" - HOLD (Not enough data)")
        continue

    today = prices[i]
    yesterday = prices[i-1]
    day_before = prices[i-2]

    if today > yesterday and yesterday > day_before:
        signal = "BUY"
    elif today < yesterday and yesterday < day_before:
        signal = "SELL"
    else:
        signal = "HOLD"
    
    print(f" - {signal}")

    print(f"    Pattern: ${day_before} → ${yesterday} → ${today}")