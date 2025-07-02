# Taking info from the user.
sleep = int(input("Hours slept: "))
study = int(input("Hours studied: "))
wasted = int(input("Hours wasted: "))

# Calculating score.
score = (study * 2) + (sleep) - (wasted * 1.5)

# Condition to find score level.
if score >=20:
    score_level = "High"
elif 10 <= score <20:
    score_level = "Medium"
else:
    score_level = "Low"

# Printing final answer.
print(f"Your productivity score is: {score}")
print(f"Level: {score_level} based on score.")