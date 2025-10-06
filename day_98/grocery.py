def main():
    # Dictionary to store item counts
    grocery_list = {}
    
    try:
        while True:
            # Get item from user
            item = input().strip().upper()
            
            # Add to dictionary or increment count
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
                
    except EOFError:
        # When user presses control-d, display the list
        print()  # Print newline
        
        # Sort items alphabetically and display
        for item in sorted(grocery_list.keys()):
            print(f"{grocery_list[item]} {item}")


if __name__ == "__main__":
    main()