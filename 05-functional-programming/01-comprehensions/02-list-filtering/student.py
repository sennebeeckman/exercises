from movie import *

def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year == year]

def movies_with_actor(movies, actor):
    return [movie.title for movie in movies if actor in movie.actors]

def divisors(n):
    return [number for number in range(1,n+1) if n%number == 0]

