def middle(ns):
    index = int((len(ns) + 1) / 2)
    return ns[index - 1]

def median(ns):
    ns = sorted(ns)
    if (len(ns) % 2) == 0:
        n1 = ns[int(len(ns) / 2) -1]
        n2 = ns[int((len(ns) / 2))]
        sum = n1 + n2
        avg = sum/2
        return avg
    else:
        return middle(ns)