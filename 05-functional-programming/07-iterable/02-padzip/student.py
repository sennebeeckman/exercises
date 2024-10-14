class PadZip:
    def __init__(self, it1, it2, padding = None):
        self.it1 = iter(it1)
        self.it2 = iter(it2)
        self.pad = padding
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        runnout = 0

        try:
            left = next(self.it1)
        except StopIteration:
            left = self.pad
            runnout += 1
        
        try:
            right = next(self.it2)
        except StopIteration:
            right = self.pad
            runnout += 1
        
        if runnout == 2:
            raise StopIteration
        
        return (left, right)


