def count_movies(watch_history):
    movie_count = {}
    
    for movie in watch_history:
        if movie in movie_count:
            movie_count[movie] += 1
        else:
            movie_count[movie] = 1

    for movie in movie_count:
        print(f"{movie}: {movie_count[movie]}")

watch_history = ["Inception", "Titanic", "Inception", "Avatar", "Titanic"]
count_movies(watch_history)