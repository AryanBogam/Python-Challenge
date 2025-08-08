def show_typing_status(contact_name, is_typing):
    if is_typing == True:
        return f"{contact_name} is typing..."
    else:
        return f"{contact_name} is not typing"

result = show_typing_status("Aryan", True)
print(result)

result2 = show_typing_status("Riya", False)
print(result2)

result3 = show_typing_status("Mom", True)
print(result3)