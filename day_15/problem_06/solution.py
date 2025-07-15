def multiplication_table():
    try:
        number = int(input("Enter number: "))
        rows = int(input("Enter number of rows: "))
        
        if number <= 0 or rows <= 0:
            print("Error: Inputs must be positive integers")
            return
        
        if rows > 20:
            print("Error: Cannot generate more than 20 rows")
            return
        
        for i in range(1, rows + 1):
            print(f"{number} × {i} = {number * i}")
    
    except ValueError:
        print("Error: Please enter valid integers")
multiplication_table()