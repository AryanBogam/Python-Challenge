def add_cleaning_fee(booking_total, cleaning_fee):
    updated_total = booking_total + cleaning_fee
    return updated_total

booking_total = 300
cleaning_fee = 50
result = add_cleaning_fee(booking_total, cleaning_fee)
print(result)

print(add_cleaning_fee(250, 30))
print(add_cleaning_fee(400, 75))
print(add_cleaning_fee(150, 25))