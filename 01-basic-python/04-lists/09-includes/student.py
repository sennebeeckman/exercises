def includes(xs, ys):
    target = len(ys)
    for y in ys:
        if y in xs:
            target -= 1
    if target == 0:
        return True
    else:
        return False
