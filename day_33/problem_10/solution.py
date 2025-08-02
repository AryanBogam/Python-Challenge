def generate_announcement(train_no, station, platform, delay=0):
    if delay == 0:
        announcement = f"Train {train_no} is arriving at {station} on platform {platform}."
    else:
        announcement = f"Train {train_no} is delayed by {delay} minutes and will arrive at {station} on platform {platform}."
    
    print(announcement)
    return announcement

test_cases = [
    ("12903", "Mumbai", 5),
    ("22120", "Delhi", 3, 10),
    ("18520", "Chennai", 2, 25),
    ("12050", "Bangalore", 1)
]

print("RAILWAY ANNOUNCEMENT GENERATOR")
print("-" * 40)

for case in test_cases:
    if len(case) == 3:
        train_no, station, platform = case
        generate_announcement(train_no, station, platform)
    else:
        train_no, station, platform, delay = case
        generate_announcement(train_no, station, platform, delay)
    print()

print("="*40)
print("GENERATE CUSTOM ANNOUNCEMENT")
train_no = input("Enter train number: ")
station = input("Enter station name: ")
try:
    platform = int(input("Enter platform number: "))
    delay_input = input("Enter delay in minutes (press Enter for no delay): ")
    
    if delay_input.strip() == "":
        delay = 0
    else:
        delay = int(delay_input)
    
    print("\nAnnouncement:")
    print("-" * 20)
    generate_announcement(train_no, station, platform, delay)
    
except ValueError:
    print("Please enter valid numbers")