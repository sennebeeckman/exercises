from itertools import permutations
from more_itertools import pairwise

def find_shortest_path(distance, city_count):
    def total_distance(path):
        return sum(distance(x, y) for x, y in pairwise(path))
    paths = ([0, *p, 0] for p in permutations(range(1, city_count)))
    return min(paths, key=total_distance)