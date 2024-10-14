def cycle(xs):
    lijst = list(xs)
    while True:
        for value in lijst:
            yield value

