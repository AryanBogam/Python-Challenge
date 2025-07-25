class WeakPasswordError(Exception):
    pass

def check_password(password):
    if len(password) < 8:
        raise WeakPasswordError()

password = input("Enter password: ")

try:
    check_password(password)
    print("Good password!")
except WeakPasswordError:
    print("Password too short!")