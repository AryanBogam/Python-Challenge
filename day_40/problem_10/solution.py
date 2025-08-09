def check_vip_status(vip_list, username):
    if username in vip_list:
        return f"{username} is a VIP!"
    else:
        return f"{username} is not a VIP"

vip_list = ["Aryan", "Riya", "John", "Alice"]
result = check_vip_status(vip_list, "Aryan")
print(result)

result2 = check_vip_status(vip_list, "Bob")
print(result2)

result3 = check_vip_status(vip_list, "Riya")
print(result3)