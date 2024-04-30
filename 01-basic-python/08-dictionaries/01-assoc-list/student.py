class AssocList():

    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        for x in self.__items:
            if x[0] == key:
                x[1] = value
                return
        self.__items.append([key, value])

    def __getitem__(self, key):
        for x in self.__items:
            if x[0] == key:
                return x[1]
            else:
                continue
        raise KeyError()
    
    def __contains__(self, key):
        for x in self.__items:
            if x[0] == key:
                return True
            else:
                continue
        return False
            
    def __len__(self):
        return len(self.__items)
    
    @property
    def keys(self):
        keys_list = []
        for x in self.__items:
            keys_list.append(x[0])
        return keys_list
    
    @property
    def values(self):
        values_list = []
        for x in self.__items:
            values_list.append(x[1])
        return values_list
    
test_assoc = AssocList()
