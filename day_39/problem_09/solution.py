def organize_chats(chats):
    organized_list = []
    for chat in chats:
        if chat["pinned"] == True:
            organized_list.append(f"Pinned: {chat['name']}")
    for chat in chats:
        if chat["pinned"] == False:
            organized_list.append(chat["name"])
    return organized_list

chats = [
    {"name": "Friend", "pinned": False},
    {"name": "Mom", "pinned": True},
    {"name": "Cousin", "pinned": False},
    {"name": "Work", "pinned": True}
]

result = organize_chats(chats)
print(result)

chats2 = [
    {"name": "Alice", "pinned": False},
    {"name": "Boss", "pinned": True},
    {"name": "Bob", "pinned": False}
]

result2 = organize_chats(chats2)
print(result2)