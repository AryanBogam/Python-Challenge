usd_amounts = [1, 5, 10]
exchange_rate = 83

inr_amounts = []
for amount in usd_amounts:
    inr = amount * exchange_rate
    inr_amounts.append(inr)

print(inr_amounts)