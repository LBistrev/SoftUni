class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.last_number = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_number <= 0:
            raise StopIteration
        self.last_number -= 1
        return self.last_number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
