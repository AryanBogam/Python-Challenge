events = []

while True:
    print("1. Create event")
    print("2. Invite friends")
    print("3. View all events")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        event_name = input("Enter event name: ")
        event_date = input("Enter event date: ")
        events.append({"name": event_name, "date": event_date, "invited": []})
        print("Event created!")
    
    elif choice == "2":
        event_name = input("Enter event name: ")
        friend_name = input("Enter friend to invite: ")
        
        for event in events:
            if event["name"] == event_name:
                event["invited"].append(friend_name)
                print("Friend invited!")
                break
        else:
            print("Event not found!")
    
    elif choice == "3":
        print("All events:")
        for event in events:
            print("Event:", event["name"])
            print("Date:", event["date"])
            print("Invited friends:", event["invited"])
            print()
    
    elif choice == "4":
        break