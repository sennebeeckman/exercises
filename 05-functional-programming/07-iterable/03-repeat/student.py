class Repeat:
    def __init__(self, element):
        self.element = element

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.element
