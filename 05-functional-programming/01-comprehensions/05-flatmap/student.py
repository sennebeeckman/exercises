from movie import *
from util import Card

def genres(movies):
    return {genre for movie in movies for genre in movie.genres}

def actors(movies):
    return {actor for movie in movies for actor in movie.actors }

def repeat_consecutive(xs, n):
    return [x for x in xs for s in range(1,n+1)]

def repeat_alternating(xs, n):
    return [x for s in range(1,n+1) for x in xs ]

def cards(values, suits):
    return {Card(value, suit) for suit in suits for value in values}
