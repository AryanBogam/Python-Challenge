def most_popular_place_today(checkins):
    place_count = {}
    
    for user, location, time in checkins:
        if location in place_count:
            place_count[location] += 1
        else:
            place_count[location] = 1
    
    return max(place_count, key=place_count.get)

checkins = [
    ("user1", "Starbucks", "today"),
    ("user2", "McDonald's", "today"),
    ("user3", "Starbucks", "today"),
    ("user4", "Starbucks", "today")
]

print(most_popular_place_today(checkins))