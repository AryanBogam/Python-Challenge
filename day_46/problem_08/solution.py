def check_minimum_stay(min_nights, nights):
    if nights < min_nights:
        return "Too short"
    else:
        return "Booking allowed"

min_nights = 2
nights = 1
result = check_minimum_stay(min_nights, nights)
print(result)

print(check_minimum_stay(3, 5))
print(check_minimum_stay(7, 7))
print(check_minimum_stay(2, 1))
print(check_minimum_stay(1, 3))