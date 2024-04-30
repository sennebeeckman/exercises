def contains_duplicates(xs):
    checked = []
    for number in xs:
        if number in checked:
            return True
        else:
            checked.append(number)
            continue
    return False