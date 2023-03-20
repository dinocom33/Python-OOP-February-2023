class vowels:
    VOWELS = ["a", "e", "i", "o", "u", "y"]

    def __init__(self, string):
        self.string = list(string)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.string):

            result = self.string[self.idx]

            self.idx += 1

            if result.lower() in self.VOWELS:
                return result
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
