def vowel_filter(function):

    def wrapper():

        vowels = ["a", "e", "i", "o", "u", "y"]
        func = function()
        result = [ch for ch in func if ch.lower() in vowels]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
