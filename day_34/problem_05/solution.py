capital = 1000000
final_value = 1200000

print("Hedge Fund Fee Calculation:")
print(f"Initial Capital: ${capital:,}")
print(f"Final Value: ${final_value:,}")

management_fee = capital * 0.02
print(f"\nManagement Fee (2%): ${management_fee:,}")

profit = final_value - capital
print(f"Profit: ${profit:,}")

performance_fee = profit * 0.20
print(f"Performance Fee (20% of profit): ${performance_fee:,}")

total_fees = management_fee + performance_fee
print(f"\nTotal Fees: ${total_fees:,}")

investor_keeps = final_value - total_fees
print(f"Investor Keeps: ${investor_keeps:,}")