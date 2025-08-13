def simulate_function_trigger(event_type):
    if event_type == "http":
        return "HTTP Trigger Function executed"
    elif event_type == "timer":
        return "Timer Trigger Function executed"
    elif event_type == "blob":
        return "Blob Trigger Function executed"
    else:
        return "Unknown trigger type"

event = "http"
result = simulate_function_trigger(event)
print(result)

trigger_types = ["http", "timer", "blob", "queue"]

for trigger in trigger_types:
    message = simulate_function_trigger(trigger)
    print(f"{trigger} -> {message}")

def process_events(events):
    for event in events:
        message = simulate_function_trigger(event)
        print(f"Event '{event}': {message}")

events = ["http", "timer", "blob", "http", "timer"]
print("\nProcessing multiple events:")
process_events(events)