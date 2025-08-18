playlist = ["Song1", "Song2", "Song3"]
current = "Song3"
action = "next"

current_index = 0
for i in range(len(playlist)):
    if playlist[i] == current:
        current_index = i

if action == "next":
    next_index = current_index + 1
    if next_index >= len(playlist):
        next_index = 0
else:
    next_index = current_index - 1
    if next_index < 0:
        next_index = len(playlist) - 1

print(playlist[next_index])