class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.count:
            raise StopIteration
        self.counter += 1
        temp = self.start
        self.start += self.step
        return temp