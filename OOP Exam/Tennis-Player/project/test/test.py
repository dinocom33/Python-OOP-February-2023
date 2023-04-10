from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Jon", 20, 10)

    def test_correct_initialization(self):
        self.assertEqual(self.player.name, "Jon")
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.points, 10)
        self.assertEqual(self.player.wins, [])

    def test_set_name_with_less_than_two_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Mi", 30, 15)

        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_add_age_with_incorrect_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Mike", 17, 25)

        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win(self):
        self.player.add_new_win("Australia Open")
        self.player.add_new_win("Sofia Open")

        self.assertEqual(self.player.wins, ["Australia Open", "Sofia Open"])

    def test_add_existing_new_win(self):
        self.player.add_new_win("Sofia Open")
        self.player.add_new_win("Australia Open")

        result = self.player.add_new_win("Australia Open")

        self.assertEqual(self.player.wins, ["Sofia Open", "Australia Open"])
        self.assertEqual(result, "Australia Open has been already added to the list of wins!")

    def test__lt__returns_other_player_is_better(self):
        other = TennisPlayer("Mike", 20, 50)

        result = self.player.__lt__(other)

        self.assertEqual(result, 'Mike is a top seeded player and he/she is better than Jon')

    def test__LT__returns_first_player_is_better(self):
        other = TennisPlayer("Mike", 20, 5)

        result = self.player.__lt__(other)

        self.assertEqual(result, 'Jon is a better player than Mike')

    def test__str__returns_correct_string(self):
        self.player.add_new_win("Sofia Open")
        self.player.add_new_win("Australia Open")

        result = str(self.player)

        self.assertEqual(result, f"Tennis Player: {self.player.name}\n" +
                                 f"Age: {self.player.age}\n" +
                                 f"Points: {self.player.points:.1f}\n" +
                                 f"Tournaments won: {', '.join(self.player.wins)}")


if __name__ == '__main__':
    main()
