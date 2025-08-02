train_to_platform = {
    "12903": 1,
    "12050": 2
}

def assign_platform(train_no, platform_no):
    if train_no in train_to_platform:
        current_platform = train_to_platform[train_no]
        print(f"Warning: Train {train_no} is already assigned to Platform {current_platform}")
        return False
    else:
        train_to_platform[train_no] = platform_no
        print(f"Platform {platform_no} assigned to Train {train_no}")
        return True

def show_assignments():
    print("Current Platform Assignments:")
    print("-" * 30)
    for train, platform in train_to_platform.items():
        print(f"Train {train} → Platform {platform}")

print("PLATFORM ASSIGNMENT SYSTEM")
print("=" * 35)

show_assignments()

print("\nTesting assignments:")

assign_platform("12903", 3)
assign_platform("22120", 3)
assign_platform("18520", 4)
print()
show_assignments()

print("\n" + "="*35)
print("ASSIGN NEW PLATFORM")
train_no = input("Enter train number: ")
try:
    platform_no = int(input("Enter platform number: "))
    assign_platform(train_no, platform_no)
except ValueError:
    print("Please enter valid platform number")