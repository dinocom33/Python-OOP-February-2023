from itertools import permutations


def possible_permutations(numbers_list):
    for elements in list(permutations(numbers_list)):
        yield list(elements)


[print(n) for n in possible_permutations([1, 2, 3])]
