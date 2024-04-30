def drop_ends(xs):
    if len(xs) > 2:
        xs = xs[1:]
        print(xs)
        print(len(xs))
        print(xs[0])
        xs = xs[:len(xs)-1]
    else:
        xs = []
    return xs
