traffic = {
    "north": 30,
    "south": 80,
    "east": 40,
    "west": 25
}

max_dir = max(traffic, key=traffic.get)
print(f"Allow traffic from {max_dir} first")