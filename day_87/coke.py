def main():
    # Cost of a Coke in cents
    cost = 50
    
    # Amount due starts at 50 cents
    amount_due = cost
    
    print("Amount Due:", amount_due)
    
    while amount_due > 0:
        print("Insert Coin: ", end="")
        try:
            coin = int(input())
        except ValueError:
            # If input is not a valid integer, continue asking
            continue
        
        # Check if coin is a valid denomination
        if coin in [25, 10, 5]:
            amount_due -= coin
            if amount_due > 0:
                print("Amount Due:", amount_due)
        else:
            # Invalid coin, show current amount due
            print("Amount Due:", amount_due)
    
    # Calculate change owed (amount_due will be negative or zero)
    change = abs(amount_due)
    print("Change Owed:", change)

if __name__ == "__main__":
    main()