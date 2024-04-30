def contains_duplicates(ns):
    checked = []
    dup = []
    for number in ns:
        if number in checked:
            dup.append(number)
            continue
        else:
            checked.append(number)
            continue
    return dup

def target_sum(ns, target):
    for x in ns:
        for y in ns:
            if y != x or y in contains_duplicates(ns):
                if x + y == target:
                    return True
            else:
                continue
    return False
