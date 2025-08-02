train_seats = {
    "12903": {"SL": 120, "3A": 50, "2A": 30},
    "22120": {"SL": 80, "3A": 40, "2A": 10}
}

def check_seat_availability(train_no, class_type):
    if train_no not in train_seats:
        return "Train not found"
    
    if class_type not in train_seats[train_no]:
        return "Class not available"
    
    available_seats = train_seats[train_no][class_type]
    
    if available_seats > 0:
        return f"{available_seats} seats available"
    else:
        return "No seats available"

test_cases = [
    ("12903", "SL"),
    ("12903", "2A"),
    ("99999", "SL"),
    ("12903", "1A")
]

print("SEAT AVAILABILITY CHECKER")
print("-" * 30)

for train, class_type in test_cases:
    result = check_seat_availability(train, class_type)
    print(f"Train {train}, Class {class_type}: {result}")

print("\n" + "="*30)
train_no = input("Enter train number: ")
class_type = input("Enter class (SL/3A/2A): ")
result = check_seat_availability(train_no, class_type)
print(f"Result: {result}")