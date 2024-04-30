def is_increasing(ns):
    value = True
    if len(ns) > 1:
        ms = ns[1:]
        print(ms)
        result = list(zip(ns, ms))
        for x in result:
            if x[0] <= x[1]:
                value = True
            else:
                value = False
                return value
    return value
