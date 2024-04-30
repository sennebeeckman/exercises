def odd_keys_dict(dict):
    dict2 = {}
    for x in dict:
        print(x)
        if x%2 != 0:
            dict2.update({x: dict[x]})
    return dict2
