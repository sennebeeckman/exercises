from movie import *

def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}

def director_to_titles(movies):
    return {movie.director: [movie2.title for movie2 in movies if movie.director == movie2.director] for movie in movies}