class Even:
    def __init__(self,limit):
        self.num = 0
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < self.limit: 
            self.num += 2
            return self.num
        else:
            raise StopIteration

class Odd:
    def __init__(self,limit):
        self.num = -1;
        self.limit = limit
    
    def __iter__(self):
        return self
    def __next__(self):
        val = self.num+2
        if val <= self.limit:
            self.num = val
            return self.num
        else:
            raise StopIteration
e = list(Even(10))
o = list(Odd(10))
print(e)
print(o)