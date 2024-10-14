class InclusiveRange:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __iter__(self):
        return InclusiveRangeIterator(self.begin, self.end)

class InclusiveRangeIterator:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.begin <= self.end:
            x = self.begin
            self.begin += 1
            return x
        else:
            raise StopIteration()
