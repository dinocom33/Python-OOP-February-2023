class reverse_iter:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.idx = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < 0:
            raise StopIteration

        result = self.iterable[self.idx]
        self.idx -= 1

        return result


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
