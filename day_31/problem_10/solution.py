memory = 0

def process_command(command):
    global memory
    
    parts = command.split()
    if len(parts) == 0:
        return "Invalid command"
    
    operation = parts[0].lower()
    
    if operation == "add" and len(parts) == 2:
        try:
            value = float(parts[1])
            memory += value
            return f"Added {value}. Memory: {memory}"
        except ValueError:
            return "Invalid number"
    
    elif operation == "sub" and len(parts) == 2:
        try:
            value = float(parts[1])
            memory -= value
            return f"Subtracted {value}. Memory: {memory}"
        except ValueError:
            return "Invalid number"
    
    elif operation == "mult" and len(parts) == 2:
        try:
            value = float(parts[1])
            memory *= value
            return f"Multiplied by {value}. Memory: {memory}"
        except ValueError:
            return "Invalid number"
    
    elif operation == "reset":
        memory = 0
        return "Memory reset to 0"
    
    elif operation == "show":
        return f"Current memory: {memory}"
    
    else:
        return "Invalid command. Use: add/sub/mult [number], reset, show"

commands = ["add 5", "sub 2", "mult 3", "show", "reset", "show"]

print("CALCULATOR WITH MEMORY")
print("-" * 30)

for cmd in commands:
    result = process_command(cmd)
    print(f"Command: {cmd}")
    print(f"Result: {result}")
    print()