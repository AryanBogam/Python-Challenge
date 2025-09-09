users = {
    "john": {"email": "john@email.com"},
    "jane": {"email": "jane@email.com"},
    "bob": {"email": "bob@email.com"}
}
logged_in_users = ["john", "jane", "bob"]
events = []

def create_event(creator, title, date, location):
    if creator not in logged_in_users:
        return "Please log in first!"
    
    event = {
        "id": len(events) + 1,
        "creator": creator,
        "title": title,
        "date": date,
        "location": location,
        "going": [creator],
        "interested": []
    }
    events.append(event)
    return "Event created successfully!"

def rsvp_event(username, event_id, response):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if response not in ["going", "interested"]:
        return "Invalid response! Use 'going' or 'interested'"
    
    for event in events:
        if event["id"] == event_id:
            if username in event["going"]:
                event["going"].remove(username)
            if username in event["interested"]:
                event["interested"].remove(username)
            
            event[response].append(username)
            return f"RSVP updated to {response}!"
    
    return "Event not found!"

def get_user_events(username):
    if username not in logged_in_users:
        return "Please log in first!"
    
    user_events = []
    for event in events:
        if username in event["going"] or username in event["interested"]:
            user_events.append(event)
    
    return user_events

print(create_event("john", "Python Workshop", "2023-12-25", "New York"))
print(rsvp_event("jane", 1, "going"))
print(rsvp_event("bob", 1, "interested"))

print("Jane's events:", len(get_user_events("jane")))
print("Event details:", events[0])