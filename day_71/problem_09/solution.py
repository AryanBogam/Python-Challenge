users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"},
    "bob": {"email": "bob@email.com", "password": "pass789"}
}
logged_in_users = ["john", "jane", "bob"]
groups = {}

def create_group(creator, group_name):
    if creator not in logged_in_users:
        return "Please log in first!"
    
    if group_name in groups:
        return "Group name already exists!"
    
    groups[group_name] = {
        "creator": creator,
        "members": [creator],
        "posts": []
    }
    return "Group created successfully!"

def join_group(username, group_name):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if group_name not in groups:
        return "Group not found!"
    
    if username in groups[group_name]["members"]:
        return "Already a member!"
    
    groups[group_name]["members"].append(username)
    return "Joined group successfully!"

def post_in_group(username, group_name, content):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if group_name not in groups:
        return "Group not found!"
    
    if username not in groups[group_name]["members"]:
        return "You are not a member of this group!"
    
    post = {"author": username, "content": content}
    groups[group_name]["posts"].append(post)
    return "Posted in group successfully!"

print(create_group("john", "Python Lovers"))
print(join_group("jane", "Python Lovers"))
print(post_in_group("jane", "Python Lovers", "Love coding in Python!"))
print(groups)