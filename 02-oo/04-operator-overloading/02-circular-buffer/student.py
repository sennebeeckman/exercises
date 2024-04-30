class CircularBuffer:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__buffer = []

    def __len__(self):
        return len(self.__buffer)
    
    def add(self, item):
        self.__buffer.append(item) 
        if len(self) > self.__max_size:
            del self.__buffer[0]
            

    def __getitem__(self, index):
        return self.__buffer[index]
