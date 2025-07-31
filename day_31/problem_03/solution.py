weights = [300, 750, 1200, 2500, 450, 3000, 800]

categories = {
    "Light": [],
    "Medium": [],
    "Heavy": []
}

for weight in weights:
    if weight < 500:
        categories["Light"].append(weight)
    elif weight <= 2000:
        categories["Medium"].append(weight)
    else:
        categories["Heavy"].append(weight)

print("Parcel Weight Categories:")
print("-" * 30)
for category, weight_list in categories.items():
    print(f"{category}: {weight_list}")
    print(f"Count: {len(weight_list)}")
    print()