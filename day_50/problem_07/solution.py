event1 = ["Alice", "Bob", "Eve"]
event2 = ["Eve", "Charlie", "Bob"]

common_attendees = []
for person in event1:
    if person in event2:
        common_attendees.append(person)

print(common_attendees)