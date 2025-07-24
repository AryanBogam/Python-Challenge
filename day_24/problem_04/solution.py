movies = [
    {"title": "The Dark Knight", "rating": 9.0, "genre": "Action"},
    {"title": "Inception", "rating": 8.8, "genre": "Sci-Fi"},
    {"title": "The Godfather", "rating": 9.2, "genre": "Drama"},
    {"title": "Interstellar", "rating": 8.6, "genre": "Sci-Fi"}
]

new_movie = {"title": "Avatar", "rating": 7.8, "genre": "Sci-Fi"}
movies.append(new_movie)
print("Added new movie:", new_movie["title"])

search_genre = "Sci-Fi"
print(f"\n{search_genre} movies:")
for movie in movies:
    if movie["genre"] == search_genre:
        print(f"{movie['title']} - {movie['rating']}")

for i in range(len(movies)):
    for j in range(len(movies) - 1):
        if movies[j]["rating"] < movies[j + 1]["rating"]:
            movies[j], movies[j + 1] = movies[j + 1], movies[j]

print("\nMovies sorted by rating:")
for movie in movies:
    print(f"{movie['title']} - {movie['rating']}")