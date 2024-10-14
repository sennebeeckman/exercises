class Cycle:
    def __init__(self, element):
        self.element = list(element)
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        x = self.element[self.counter]
        if (self.counter + 1) == (len(self.element)):
            self.counter = 0
        else:
            self.counter += 1
        return x
    