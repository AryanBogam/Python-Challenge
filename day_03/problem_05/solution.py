# Creating two tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# Calculating sums comparing
sum1 = sum(tuple1)
sum2 = sum(tuple2)

# It is comparing
is_sum1_less = sum1 < sum2

print(f"Sum of tuple1: {sum1}")
print(f"Sum of tuple2: {sum2}")
print(f"Is sum of tuple1 less than sum of tuple2? {is_sum1_less}")

# Concatenating tuples
combined_tuple = tuple1 + tuple2
print(f"Combined tuple: {combined_tuple}")