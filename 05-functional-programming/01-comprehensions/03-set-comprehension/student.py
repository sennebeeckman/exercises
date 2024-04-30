from movie import *

def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, xy):
    return {s for s in xs if s in xy}