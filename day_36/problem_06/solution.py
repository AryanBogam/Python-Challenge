def check_trending(views_today):
    if views_today > 50000:
        return "Trending"
    else:
        return "Not Trending"

views_today = 52000
result = check_trending(views_today)
print(result)

views_today2 = 30000
result2 = check_trending(views_today2)
print(result2)