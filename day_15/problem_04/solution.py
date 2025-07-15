def secure_door():
    passcode = input("Enter 4-digit passcode: ")
    word = input("Enter security word: ")
    
    if not (passcode.isdigit() and len(passcode) == 4):
        print("Error: Passcode must be a 4-digit number")
        return
    
    if any(char.isdigit() for char in word):
        print("Error: Security word must not contain digits")
        return
    
    print("Access granted")

secure_door()