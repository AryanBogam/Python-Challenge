def filter_action_shows(shows):
    action_shows = []
    for show in shows:
        genre = shows[show]
        if genre == "Action":
            action_shows.append(show)
    return action_shows

shows = {"Money Heist": "Action", "Friends": "Comedy", "Extraction": "Action"}
result = filter_action_shows(shows)
print(result)

shows2 = {"The Avengers": "Action", "The Office": "Comedy", "John Wick": "Action", "Breaking Bad": "Drama"}
result2 = filter_action_shows(shows2)
print(result2)