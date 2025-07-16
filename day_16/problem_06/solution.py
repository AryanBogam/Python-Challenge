def parse_command(command):
    command_lower = command.lower()
    
    # Extract action
    if "turn on" in command_lower:
        action = "turn on"
    elif "turn off" in command_lower:
        action = "turn off"
    else:
        action = None
    
    # Extract device
    if "lights" in command_lower:
        device = "lights"
    elif "tv" in command_lower:
        device = "tv"
    else:
        device = None
    
    # Extract location
    if "living room" in command_lower:
        location = "living room"
    elif "bedroom" in command_lower:
        location = "bedroom"
    else:
        location = None
    
    return {"action": action, "device": device, "location": location}

result = parse_command("Turn on the living room lights")
print(result)