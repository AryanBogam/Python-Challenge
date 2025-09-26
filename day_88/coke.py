def main():
    cost = 50
    amount_due = cost
    
    print("Amount Due:", amount_due)
    
    while amount_due > 0:
        print("Insert Coin: ", end="")
        try:
            coin = int(input())
        except ValueError:
            continue

        if coin in [25, 10, 5]:
            amount_due -= coin
            if amount_due > 0:
                print("Amount Due:", amount_due)
        else:
            print("Amount Due:", amount_due)
            
    change = abs(amount_due)
    print("Change Owed:", change)

if __name__ == "__main__":
    main()