from typing import List


def get_primes(numbers: List[int]):
    for num in numbers:
        if num <= 1:
            continue

        for number in range(2, num // 2 + 1):
            if num % number == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
