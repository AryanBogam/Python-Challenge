def find_top_donor(donors):
    top_donor = ""
    highest_amount = 0
    for donor in donors:
        amount = donors[donor]
        if amount > highest_amount:
            highest_amount = amount
            top_donor = donor
    return top_donor

donors = {"Aryan": 50, "John": 120, "Zoe": 90}
result = find_top_donor(donors)
print(result)

donors2 = {"Alice": 200, "Bob": 150, "Charlie": 300, "Diana": 75}
result2 = find_top_donor(donors2)
print(result2)