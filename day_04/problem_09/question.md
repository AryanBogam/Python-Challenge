Question 9: Customer Preference Analyzer – E-Commerce Logic

Scenario:
You're building an analytics feature for an e-commerce platform to understand customer behavior.

bought_electronics = {"Aryan", "Riya", "Om", "Sahil"}
bought_clothing = {"Om", "Tina", "Sahil", "Meera"}
all_customers = {"Aryan", "Riya", "Om", "Sahil", "Tina", "Meera", "Aditya"}

Determine:

Customers who bought both electronics and clothing
Customers who bought only electronics
Customers who haven’t bought either

Expected Logic:

Use intersection() for both
Use difference() for only electronics
Use union of both categories to filter out non-buyers