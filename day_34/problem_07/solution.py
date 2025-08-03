returns = [0.01, 0.015, -0.005, 0.012, 0.02]
risk_free = 0.005

print("Daily Returns:", returns)
print(f"Risk-Free Rate: {risk_free}")

mean_return = sum(returns) / len(returns)
print(f"\nMean Return: {mean_return:.4f}")

differences = []
for return_val in returns:
    diff = return_val - mean_return
    differences.append(diff)

squared_diffs = []
for diff in differences:
    squared_diffs.append(diff * diff)

variance = sum(squared_diffs) / len(squared_diffs)

import math
std_dev = math.sqrt(variance)

print(f"Standard Deviation: {std_dev:.4f}")

excess_return = mean_return - risk_free
sharpe_ratio = excess_return / std_dev

print(f"\nExcess Return: {excess_return:.4f}")
print(f"Sharpe Ratio: {sharpe_ratio:.4f}")

if sharpe_ratio > 1:
    print("Good risk-adjusted return!")
elif sharpe_ratio > 0:
    print("Okay risk-adjusted return")
else:
    print("Poor risk-adjusted return")