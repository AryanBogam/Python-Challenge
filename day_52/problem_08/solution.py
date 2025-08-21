games = ["Cyberpunk", "Minecraft", "GTA V"]
ray_tracing_games = ["Cyberpunk", "Minecraft"]

filtered_games = []
for game in games:
    if game in ray_tracing_games:
        filtered_games.append(game)

print(filtered_games)