inventory = [10, 2, 0, 7, 4]

for i in range(len(inventory)):
    if inventory[i] < 5:
        print("Restock Needed for index", i)