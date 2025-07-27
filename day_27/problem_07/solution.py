def login(username, password):
    correct_username = "admin"
    correct_password = "123"
    
    try:
        if username == "" or password == "":
            return "Login failed"
        elif username == correct_username and password == correct_password:
            return "Login successful"
        else:
            return "Login failed"
    except:
        return "Login failed"

user = input("Username: ")
pwd = input("Password: ")
print(login(user, pwd))