logged_in_users = ["john", "jane", "bob", "alice"]
groups = {
    "python_lovers": {
        "members": {
            "john": "admin",
            "jane": "moderator", 
            "bob": "member",
            "alice": "member"
        },
        "posts": [],
        "pinned_post": None
    }
}

def create_group_with_roles(creator, group_name):
    if creator not in logged_in_users:
        return "Please log in first!"
    
    if group_name in groups:
        return "Group already exists!"
    
    groups[group_name] = {
        "members": {creator: "admin"},
        "posts": [],
        "pinned_post": None
    }
    return "Group created successfully!"

def add_member_to_group(admin, group_name, new_member, role="member"):
    if admin not in logged_in_users:
        return "Please log in first!"
    
    if group_name not in groups:
        return "Group not found!"
    
    if groups[group_name]["members"].get(admin) != "admin":
        return "Only admins can add members!"
    
    if role not in ["admin", "moderator", "member"]:
        return "Invalid role!"
    
    groups[group_name]["members"][new_member] = role
    return f"{new_member} added as {role}!"

def remove_member_from_group(admin, group_name, member_to_remove):
    if admin not in logged_in_users:
        return "Please log in first!"
    
    if group_name not in groups:
        return "Group not found!"
    
    if groups[group_name]["members"].get(admin) != "admin":
        return "Only admins can remove members!"
    
    if member_to_remove not in groups[group_name]["members"]:
        return "Member not in group!"
    
    del groups[group_name]["members"][member_to_remove]
    return f"{member_to_remove} removed from group!"

def pin_post_in_group(username, group_name, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if group_name not in groups:
        return "Group not found!"
    
    user_role = groups[group_name]["members"].get(username)
    if user_role not in ["admin", "moderator"]:
        return "Only admins and moderators can pin posts!"
    
    groups[group_name]["pinned_post"] = post_id
    return "Post pinned successfully!"

def delete_post_from_group(username, group_name, post_id):
    if username not in logged_in_users:
        return "Please log in first!"
    
    if group_name not in groups:
        return "Group not found!"
    
    user_role = groups[group_name]["members"].get(username)
    if user_role not in ["admin", "moderator"]:
        return "Only admins and moderators can delete posts!"
    
    group_posts = groups[group_name]["posts"]
    for i, post in enumerate(group_posts):
        if post["id"] == post_id:
            group_posts.pop(i)
            return "Post deleted successfully!"
    
    return "Post not found!"

def get_user_role(username, group_name):
    if group_name not in groups:
        return "Group not found!"
    
    return groups[group_name]["members"].get(username, "Not a member")

def get_group_members_by_role(group_name):
    if group_name not in groups:
        return "Group not found!"
    
    roles = {"admin": [], "moderator": [], "member": []}
    
    for member, role in groups[group_name]["members"].items():
        if role in roles:
            roles[role].append(member)
    
    return roles

print(add_member_to_group("john", "python_lovers", "charlie", "member"))
print(pin_post_in_group("jane", "python_lovers", 1))
print(pin_post_in_group("bob", "python_lovers", 2))

print("Jane's role:", get_user_role("jane", "python_lovers"))
print("Bob's role:", get_user_role("bob", "python_lovers"))

roles_breakdown = get_group_members_by_role("python_lovers")
print("Group roles:", roles_breakdown)