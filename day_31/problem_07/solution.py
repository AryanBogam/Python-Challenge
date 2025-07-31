usage_data = [("Alice", 800), ("Bob", 1200), ("Alice", 900), ("Charlie", 2000), ("Bob", 400), ("Diana", 1800)]

user_totals = {}
for user, mb_used in usage_data:
    if user not in user_totals:
        user_totals[user] = 0
    user_totals[user] += mb_used

print("MOBILE DATA USAGE REPORT")
print("-" * 40)

overuse_limit = 1500
overusers = []

for user, total_mb in user_totals.items():
    total_gb = total_mb / 1024
    status = "OVERUSE!" if total_mb > overuse_limit else "Normal"
    print(f"{user}: {total_mb}MB ({total_gb:.2f}GB) - {status}")
    
    if total_mb > overuse_limit:
        overusers.append(user)

sorted_users = sorted(user_totals.items(), key=lambda x: x[1], reverse=True)
print("\nTOP 3 USERS:")
for i, (user, mb) in enumerate(sorted_users[:3], 1):
    print(f"{i}. {user}: {mb}MB")

print(f"\nUsers with overuse: {overusers}")