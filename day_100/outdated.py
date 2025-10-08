def main():
    # List of month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    while True:
        try:
            # Get date input from user
            date_input = input("Date: ").strip()
            
            # Check if input contains a slash (MM/DD/YYYY format)
            if "/" in date_input:
                # Parse MM/DD/YYYY format
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                
            # Check if input contains a comma (Month DD, YYYY format)
            elif "," in date_input:
                # Parse "Month DD, YYYY" format
                month_day, year = date_input.split(",")
                month_name, day = month_day.strip().split(" ")
                
                # Convert month name to number
                if month_name not in months:
                    raise ValueError("Invalid month name")
                
                month = months.index(month_name) + 1  # +1 because index starts at 0
                day = int(day.strip())
                year = int(year.strip())
            else:
                # Invalid format
                raise ValueError("Invalid date format")
            
            # Validate month and day ranges
            if month < 1 or month > 12:
                raise ValueError("Invalid month")
            
            if day < 1 or day > 31:
                raise ValueError("Invalid day")
            
            # Output in YYYY-MM-DD format
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
            
        except (ValueError, AttributeError, IndexError):
            # Re-prompt on invalid input
            pass


if __name__ == "__main__":
    main()