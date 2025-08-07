def top_friends(snaps):
    friend_list = []
    for friend in snaps:
        snap_count = snaps[friend]
        friend_list.append([friend, snap_count])

    for i in range(len(friend_list)):
        for j in range(len(friend_list) - 1):
            if friend_list[j][1] < friend_list[j+1][1]:
                # Swap
                temp = friend_list[j]
                friend_list[j] = friend_list[j+1]
                friend_list[j+1] = temp

    top_3 = []
    for i in range(3):
        if i < len(friend_list):
            top_3.append(friend_list[i][0])
    return top_3

snaps = {
    "Alex": 45,
    "Riya": 70,
    "Mohan": 30,
    "Lily": 85
}

result = top_friends(snaps)
print(result)