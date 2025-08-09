def change_category(current_category, new_category):
    return f"Category changed from {current_category} to {new_category}"

result = change_category("Just Chatting", "Gaming")
print(result)

result2 = change_category("Gaming", "Art")
print(result2)

result3 = change_category("Music", "Just Chatting")
print(result3)