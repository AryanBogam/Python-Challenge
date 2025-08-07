def get_unopened_snaps(snaps):
    unopened = []
    
    for snap in snaps:
        if snap["opened"] == False:
            unopened.append(snap["from"])
    
    return unopened

snaps = [
    {"from": "zoe", "opened": True},
    {"from": "arya", "opened": False},
    {"from": "luke", "opened": False}
]

result = get_unopened_snaps(snaps)
print(result)

snaps2 = [
    {"from": "alice", "opened": False},
    {"from": "bob", "opened": True},
    {"from": "charlie", "opened": False},
    {"from": "diana", "opened": True}
]

result2 = get_unopened_snaps(snaps2)
print(result2)