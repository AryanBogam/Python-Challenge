def highest_rated(movies):
    highest_movie = ""
    highest_rating = 0
    
    for movie in movies:
        rating = movies[movie]
        if rating > highest_rating:
            highest_rating = rating
            highest_movie = movie
    
    return highest_movie

movies = {"Inception": 9.0, "Titanic": 8.5, "Avatar": 9.2}
result = highest_rated(movies)
print(result)

movies2 = {"Spider-Man": 8.0, "Batman": 9.5, "Superman": 7.5}
result2 = highest_rated(movies2)
print(result2)