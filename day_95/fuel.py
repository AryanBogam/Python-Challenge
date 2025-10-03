def main():
    while True:
        try:
            # Get fraction input from user
            fraction = input("Fraction: ")
            
            # Parse and validate the fraction
            percentage = convert(fraction)
            
            # Display the fuel gauge
            gauge_display = gauge(percentage)
            print(gauge_display)
            break
            
        except (ValueError, ZeroDivisionError):
            # Re-prompt on invalid input
            pass


def convert(fraction):
    # Split the fraction by '/'
    parts = fraction.split('/')
    
    if len(parts) != 2:
        raise ValueError("Invalid fraction format")
    
    # Convert to integers
    x = int(parts[0])
    y = int(parts[1])
    
    # Check if X is greater than Y
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")
    
    # Calculate percentage (will raise ZeroDivisionError if y is 0)
    percentage = round((x / y) * 100)
    
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()