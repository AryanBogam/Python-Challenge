meal_cost = input("How much was the meal? ")  # It is asking the cost of the meal.
meal_cost_cleaned = meal_cost.replace("$", "")  # It is replacing $ to nothing "".
final_meal_cost = float(meal_cost_cleaned)  # It is converting the string into float.

tip_percantage = input("What percentage would you like to tip? ")  # It is asking percentage of tip.
tip_percentage_cleaned = tip_percantage.replace("%", "")  # It is replacing % to nothing ""
final_tip = float(tip_percentage_cleaned)  # It is converting the string into float or int.

tip_to_live = float(final_meal_cost*final_tip/100)  # It is doing the calculation of tip in float.

print(f"Leave ${tip_to_live:.2f}")  # It is printing the cost of tip to give.