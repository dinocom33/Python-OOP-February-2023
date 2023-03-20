class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num = 0
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx != self.count:
            result = self.num
            self.num += self.step
            self.idx += 1

            return result

        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
