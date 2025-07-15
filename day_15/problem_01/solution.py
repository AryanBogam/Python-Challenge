def username_verifier():
    username = input("Enter username: ")
    
    if len(username) < 5:
        print("Username must be at least 5 characters")
        return
    
    if not username[0].isalpha():
        print("Username must start with a letter")
        return
    
    for char in username:
        if not (char.isalnum() or char == '_'):
            print("Username must only contain letters, digits, and underscore")
            return
    
    print("Username is valid!")
    
username_verifier()