rating = int(input("Rate the product (1–5): "))

if rating in [1, 2]:
    print("Poor")
elif rating == 3:
    print("Average")
elif rating == 4:
    print("Good")
elif rating == 5:
    print("Excellent")
else:
    print("Invalid rating")