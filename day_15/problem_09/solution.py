def battery_simulator():
    try:
        battery_level = int(input("Enter battery level (0-100): "))
        
        if battery_level < 0 or battery_level > 100:
            print("Battery level must be between 0-100")
            return
        
        while battery_level > 10:
            use_battery = input("Use 10% battery? (y/n): ").lower()
            if use_battery == 'y':
                battery_level -= 10
                print(f"Battery level: {battery_level}%")
            else:
                break
        
        if battery_level <= 10:
            print("Low battery. Please recharge.")
    
    except ValueError:
        print("Please enter a valid number")

# 10. Custom Exception Message Formatter
def custom_exception():
    try:
        number = float(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError:
        print("Error: Input must be a valid number!")

battery_simulator()