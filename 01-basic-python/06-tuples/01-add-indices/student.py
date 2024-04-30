def add_indices(xs):
    indices = []
    for x in range(len(xs)):
        indices.append(x)
    result = list(zip(indices, xs))
    return result