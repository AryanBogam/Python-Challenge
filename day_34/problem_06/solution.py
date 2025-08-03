values = [100000, 102000, 98000, 95000, 110000, 108000]

print("Portfolio Values:", values)

max_drawdown = 0
peak_value = values[0]

print("\nAnalyzing drawdowns:")

for i, current_value in enumerate(values):
    if current_value > peak_value:
        peak_value = current_value
    
    drawdown = peak_value - current_value
    
    print(f"Day {i+1}: ${current_value:,} (Peak: ${peak_value:,}, Drawdown: ${drawdown:,})")

    if drawdown > max_drawdown:
        max_drawdown = drawdown

print(f"\nMaximum Drawdown: ${max_drawdown:,}")

max_drawdown_percent = (max_drawdown / peak_value) * 100
print(f"Maximum Drawdown %: {max_drawdown_percent:.2f}%")