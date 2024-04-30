def merge_dicts(dict1, dict2):
    dict3 = {}
    for key, value in dict1.items():
        dict3[key] = value
    for key, value in dict2.items():
        dict3[key] = value
    return dict3

