def find_most_active_contact(contacts):
    most_active_name = ""
    highest_count = 0
    for contact in contacts:
        message_count = contacts[contact]
        if message_count > highest_count:
            highest_count = message_count
            most_active_name = contact
    
    return f"Most active: {most_active_name} ({highest_count} messages)"

contacts = {
    "Aryan": 45,
    "Riya": 152,
    "Mom": 89,
    "Friend": 23
}

result = find_most_active_contact(contacts)
print(result)

contacts2 = {
    "Alice": 67,
    "Bob": 34,
    "Charlie": 89,
    "Diana": 12
}

result2 = find_most_active_contact(contacts2)
print(result2)