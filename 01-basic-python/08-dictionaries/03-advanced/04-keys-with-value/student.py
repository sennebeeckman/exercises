def keys_with_value(dict, value):
    keys_list = []
    for x in dict:
        if dict[x] == value:
            keys_list.append(x)
    return keys_list
