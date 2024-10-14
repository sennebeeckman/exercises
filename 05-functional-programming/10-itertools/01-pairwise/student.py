from more_itertools import pairwise

def total_distance(path, distance):
    return sum(distance(x, y) for x, y in pairwise(path))
