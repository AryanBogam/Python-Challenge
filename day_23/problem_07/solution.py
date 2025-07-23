scores = {
    "Aryan": 89,
    "Riya": 38,
    "Om": 65,
    "Sneha": 29
}

for name, score in scores.items():
    if score >= 40:
        print(f"{name} - Pass")
    else:
        print(f"{name} - Fail")