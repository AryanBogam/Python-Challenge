# Taking info from the user.
income = int(input("Enter Monthly income: "))
expense = int(input("Enter Monthly expenses: "))
invest = int(input("Enter Monthly learning/investment amount: "))

# Calculating the Savings.
saving = income - expense - invest

# Calculating the saving amount after 5 years.
final_saving = saving*12*5

# Printing the final answer.
print(f"You save {saving} per month, In 5 year your final_saving will be {final_saving}")