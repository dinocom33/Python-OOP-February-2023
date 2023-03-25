class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTest(unittest.TestCase):

    def test_constructor_without_data(self):
        integer = IntegerList()
        self.assertEqual(integer.get_data(), [])

    def test_constructor_with_wrong_type_data(self):
        integer = IntegerList("ff", 4.5, 15.9)
        self.assertEqual(integer.get_data(), [])

    def test_constructor_with_correct_data(self):
        integer = IntegerList(1, 2, 3, "dd")
        self.assertEqual(integer.get_data(), [1, 2, 3])

    def test_get_data(self):
        integer = IntegerList(1, 2, 3, "dd")
        self.assertEqual(integer.get_data(), [1, 2, 3])

    def test_add_with_incorrect_data(self):
        integer = IntegerList(3)
        self.assertEqual(integer.get_data(), [3])
        with self.assertRaises(ValueError) as ex:
            integer.add("3")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_add_with_correct_data(self):
        integer = IntegerList(3)
        self.assertEqual(integer.get_data(), [3])

        integer.add(4)
        self.assertEqual(integer.get_data(), [3, 4])

    def test_remove_element(self):
        integer = IntegerList(3)
        integer.remove_index(0)
        self.assertEqual(integer.get_data(), [])

    def test_remove_element_invalid_index(self):
        integer = IntegerList(3)
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_remove_returns_removed_element(self):
        integer = IntegerList(3)
        element = integer.remove_index(0)
        self.assertEqual(element, 3)

    def test_get_with_invalid_index(self):
        integer = IntegerList(3)
        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual(str(ex.exception), "Index is out of range")

        with self.assertRaises(IndexError) as ex:
            integer.get(1)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_get_valid_index(self):
        integer = IntegerList(3)
        result = integer.get(0)
        self.assertEqual(result, 3)

    def test_insert_invalid_index(self):
        integer = IntegerList(3)
        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 1)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_insert_invalid_data(self):
        integer = IntegerList(3)
        with self.assertRaises(ValueError) as ex:
            integer.insert(0, "1")
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_insert_valid_data(self):
        integer = IntegerList(3)
        integer.insert(0, 1)
        self.assertEqual(integer.get_data(), [1, 3])

    def test_get_biggest_element(self):
        integer = IntegerList(1, 2, -3, 0, 400, 250, -320, -450)
        element = integer.get_biggest()
        self.assertEqual(element, 400)

    def test_get_index(self):
        integer = IntegerList(1, 2, -3, 0, 400, 250, -320, -450)
        result = integer.get_index(-3)
        self.assertEqual(result, 2)

        result = integer.get_index(-320)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
