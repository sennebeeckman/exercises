def take_while(xs, condition):
    for x in xs:
        if not condition(x):
            return (xs[:xs.index(x)], xs[xs.index(x):])
    return (xs, [])