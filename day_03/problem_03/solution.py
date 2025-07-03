# ✅ Step-by-step solution
months = (
    ("Jan", 31), ("Feb", 28), ("Mar", 31), ("Apr", 30),
    ("May", 31), ("Jun", 30), ("Jul", 31), ("Aug", 31),
    ("Sep", 30), ("Oct", 31), ("Nov", 30), ("Dec", 31)
)

month_input = input("Enter month (e.g., Jan): ")

found = False
for m, d in months:
    if m.lower() == month_input.lower():
        print(f"{m} has {d} days.")
        found = True
        break

if not found:
    print("Invalid month.")
