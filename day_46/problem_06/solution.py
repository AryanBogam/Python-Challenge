def apply_last_minute_discount(total, days_until_booking):
    if days_until_booking <= 3:
        discount = total * 0.10
        discounted_total = total - discount
        return discounted_total
    else:
        return total

total = 200
days_until_booking = 2
result = apply_last_minute_discount(total, days_until_booking)
print(result)

print(apply_last_minute_discount(300, 1))
print(apply_last_minute_discount(150, 5))
print(apply_last_minute_discount(400, 3))
print(apply_last_minute_discount(250, 7))