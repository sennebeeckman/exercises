def contains_duplicates(list):
    if len(set(list)) < len(list):
        return True
    else:
        return False