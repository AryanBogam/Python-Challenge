# Given.
bought_electronics = {"Aryan", "Riya", "Om", "Sahil"}
bought_clothing = {"Om", "Tina", "Sahil", "Meera"}
all_customers = {"Aryan", "Riya", "Om", "Sahil", "Tina", "Meera", "Aditya"}

# Both electronics and clothing
both = bought_electronics & bought_clothing

# Only electronics = in electronics but not in clothing
only_electronics = bought_electronics - bought_clothing

# Neither = all_customers 
buyers = bought_electronics | bought_clothing
neither = all_customers - buyers

print("Bought both:", both)
print("Bought only electronics:", only_electronics)
print("Bought neither:", neither)
