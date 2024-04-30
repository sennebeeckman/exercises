def merge_dictionaries(d1, d2, merge_function):
    result = {}
    for k in d1.keys():
        if k in d2.keys():
            result[k] = merge_function(d1[k], d2[k])
        else:
            result[k] = d1[k]
    for k in d2.keys():
        if k in d1.keys():
            result[k] = merge_function(d1[k], d2[k])
        else:
            result[k] = d2[k]   
    return result
