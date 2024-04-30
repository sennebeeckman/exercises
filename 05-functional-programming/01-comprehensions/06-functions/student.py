from movie import *

def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])

def longest_movie_runtime_with_actor(movies, actor):
    return max(movie.runtime for movie in movies if actor in movie.actors)

def has_director_made_genre(movies, director, genre):
    return any([movie for movie in movies if movie.director == director and genre in movie.genres])

def is_prime(n):
    return len([number for number in range(1, n+1) if n%number == 0]) == 2

def is_increasing(ns):
        if len(ns) > 0:
            result = [ns[z-1] for z in range(1, len(ns)) if ns[z-1] <= ns[z]]
            result.append(ns[-1])
            return result == ns
        else:
            return True
        

def count_matching(xs, ys):
    return len([xs[z] for z in range(min(len(xs), len(ys))) if xs[z] == ys[z]])

def weighted_sum(ns, weights):
    return sum([x[0] * x[1] for x in zip(ns, weights)])

def alternating_caps(string):
    return "".join([string[x].upper() if x%2 == 0 else string[x].lower() for x in range(len(string))])

def find_repeated_words(sentence):
    words = sentence.replace(".", "").replace(",", "").replace("  ", " ").lower().split()
    words_shifted = [words[x] for x in range(1, len(words))]
    combination = zip(words, words_shifted)
    return {x[0] for x in combination if x[0] == x[1]}
    
is_increasing([1, 3, 6, 8, 9])