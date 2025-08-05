def like_percentage(likes, dislikes):
    total = likes + dislikes
    percentage = (likes / total) * 100
    return percentage

likes = 120
dislikes = 30
result = like_percentage(likes, dislikes)
print(f"{result}%")