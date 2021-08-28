class dictionary_iter:
    def __init__(self, dict):
        self.dic = dict
        self.dic_elements = list(dict.items())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.dic_elements):
            raise StopIteration
        index = self.current_index
        self.current_index += 1
        return self.dic_elements[index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
