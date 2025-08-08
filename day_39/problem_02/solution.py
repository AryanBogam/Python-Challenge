def count_unread_messages(chats):
    total_unread = 0
    for chat in chats:
        unread_count = chat["unread"]
        total_unread += unread_count
    return f"Total unread messages: {total_unread}"

chats = [
    {"name": "Mom", "unread": 5},
    {"name": "Work Group", "unread": 8},
    {"name": "Friend", "unread": 2},
    {"name": "College", "unread": 0}
]

result = count_unread_messages(chats)
print(result)

chats2 = [
    {"name": "Alice", "unread": 3},
    {"name": "Bob", "unread": 7},
    {"name": "Charlie", "unread": 1}
]

result2 = count_unread_messages(chats2)
print(result2)