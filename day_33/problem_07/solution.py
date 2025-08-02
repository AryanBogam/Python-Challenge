delays = {
    "12903": 15,
    "22120": 0,
    "12050": 55
}

def get_delayed_trains(threshold):
    delayed_trains = []
    
    for train_no, delay in delays.items():
        if delay > threshold:
            delayed_trains.append(train_no)
    
    return delayed_trains

thresholds = [0, 10, 30, 60]

print("TRAIN DELAY ANALYZER")
print("-" * 25)
print("Current delays:")
for train, delay in delays.items():
    print(f"Train {train}: {delay} minutes")

print()

for threshold in thresholds:
    delayed = get_delayed_trains(threshold)
    print(f"Trains delayed > {threshold} minutes: {delayed}")

print("\n" + "="*25)
try:
    user_threshold = int(input("Enter delay threshold (minutes): "))
    delayed_trains = get_delayed_trains(user_threshold)
    
    if delayed_trains:
        print(f"Trains delayed more than {user_threshold} minutes:")
        for train in delayed_trains:
            print(f"- Train {train}: {delays[train]} minutes")
    else:
        print(f"No trains delayed more than {user_threshold} minutes")
except ValueError:
    print("Please enter valid number")