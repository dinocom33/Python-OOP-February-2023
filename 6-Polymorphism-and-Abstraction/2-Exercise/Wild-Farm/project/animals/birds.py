from project.animals.animal import Bird
from project.food import Meat, Seed, Fruit, Vegetable


class Owl(Bird):

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def allowed_food(self):
        return [Meat, Seed, Fruit, Vegetable]

    @property
    def weight_gained(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
