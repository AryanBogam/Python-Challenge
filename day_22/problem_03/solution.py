queue = [["AI101", 1], ["EK303", 2], ["BA205", 1]]

for flight in queue:
    if flight[1] == 2:
        print(flight[0])

for flight in queue:
    if flight[1] == 1:
        print(flight[0])
