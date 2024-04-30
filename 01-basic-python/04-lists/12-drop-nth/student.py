def drop_nth(xs, n):
    ys = [*xs[:n], *xs[n+1:]]
    return ys