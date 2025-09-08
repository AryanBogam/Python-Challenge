users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"}
}
logged_in_users = ["john"]

def create_profile(username, bio, age, city, education):
    if username not in logged_in_users:
        return "Please log in first!"
    
    users[username]["profile"] = {
        "bio": bio,
        "age": age,
        "city": city,
        "education": education
    }
    return "Profile created successfully!"

def update_profile(username, bio=None, age=None, city=None, education=None):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if "profile" not in users[username]:
        return "No profile found! Create profile first!"
    
    profile = users[username]["profile"]
    if bio:
        profile["bio"] = bio
    if age:
        profile["age"] = age
    if city:
        profile["city"] = city
    if education:
        profile["education"] = education
    
    return "Profile updated successfully!"

print(create_profile("john", "Hello World!", 25, "New York", "MIT"))
print(update_profile("john", bio="Updated bio"))
print(users["john"])