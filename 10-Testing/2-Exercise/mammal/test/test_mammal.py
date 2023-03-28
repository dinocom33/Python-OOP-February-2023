from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.animal = Mammal("Pooh", "Cat", "Meow")

    def test_correct_initialization(self):
        self.assertEqual(self.animal.name, "Pooh")
        self.assertEqual(self.animal.type, "Cat")
        self.assertEqual(self.animal.sound, "Meow")
        self.assertEqual(self.animal.get_kingdom(), "animals")

    def test_make_correct_sound(self):
        result = self.animal.make_sound()
        self.assertEqual(result, "Pooh makes Meow")

    def test_get_kingdom_returns_correct_string(self):
        result = self.animal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info_returns_correct_string(self):
        result = self.animal.info()
        self.assertEqual(result, "Pooh is of type Cat")


if __name__ == "__main__":
    main()
