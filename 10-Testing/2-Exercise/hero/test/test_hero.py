from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("hero", 1, 100, 100)
        self.enemy = Hero("enemy", 1, 50, 50)

    def test_correct_initialization(self):
        self.assertEqual(self.hero.username, "hero")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_with_equal_usernames_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_with_hero_zero_health_raises_exception(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_with_enemy_zero_health_raises_exception(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ex.exception), "You cannot fight enemy. He needs to rest")

    def test_battle_with_draw_result(self):
        self.hero.health, self.hero.damage = 50, 50
        result = self.hero.battle(self.enemy)
        self.assertEqual(result, "Draw")

    def test_battle_when_hero_wins(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)
        self.assertEqual(result, "You win")

    def test_battle_when_enemy_wins(self):
        result = self.enemy.battle(self.hero)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)
        self.assertEqual(result, "You lose")

    def test__str__returns_correct_string(self):
        result = str(self.hero)
        self.assertEqual(result, "Hero hero: 1 lvl\n" +
                                 "Health: 100\n" +
                                 "Damage: 100\n")


if __name__ == '__main__':
    main()
