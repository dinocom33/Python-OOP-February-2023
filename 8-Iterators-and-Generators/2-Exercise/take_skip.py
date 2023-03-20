class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter == self.count:
            raise StopIteration

        result = self.iter * self.step
        self.iter += 1

        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
