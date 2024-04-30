def group_by(xs, key_function):
    dictionary = {}
    for x in xs:
        if key_function(x) not in dictionary.keys():
            dictionary[key_function(x)] = [x]
        else:
             dictionary[key_function(x)].append(x)   
    return dictionary
