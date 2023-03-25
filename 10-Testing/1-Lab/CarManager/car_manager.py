class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = "Toyota"
# print(car.make)



import unittest


class TestCar(unittest.TestCase):

    def test_valid_initialization(self):
        car = Car("Opel", "Vectra", 2, 10)
        self.assertEqual(car.make, "Opel")
        self.assertEqual(car.model, "Vectra")
        self.assertEqual(car.fuel_consumption, 2)
        self.assertEqual(car.fuel_capacity, 10)
        self.assertEqual(car.fuel_amount, 0)

    def test_make_with_no_data(self):

        with self.assertRaises(Exception) as ex:
            car = Car("", "Vectra", 2, 10)

        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_with_no_data(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Opel", "", 2, 10)

        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_with_zero_value(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Opel", "Vectra", 0, 10)

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Opel", "Vectra", -2, 10)

        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_with_zero_value(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Opel", "Vectra", 2, 0)

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Opel", "Vectra", 2, -10)

        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_with_negative_value(self):
        car = Car("Opel", "Vectra", 2, 10)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_with_zero_amount(self):
        car = Car("Opel", "Vectra", 2, 10)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_with_negative_amount(self):
        car = Car("Opel", "Vectra", 2, 10)
        with self.assertRaises(Exception) as ex:
            car.refuel(-5)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_with_amount_bigger_than_capacity(self):
        car = Car("Opel", "Vectra", 2, 10)
        car.refuel(20)
        self.assertEqual(car.fuel_amount, 10)

    def test_refuel_with_valid_amount(self):
        car = Car("Opel", "Vectra", 2, 10)
        car.refuel(5)
        self.assertEqual(car.fuel_amount, 5)

    def test_drive_with_bigger_distance_than_fuel_amount(self):
        car = Car("Opel", "Vectra", 2, 5)
        with self.assertRaises(Exception) as ex:
            car.drive(500)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_with_valid_distance(self):
        car = Car("Opel", "Vectra", 10, 50)
        car.fuel_amount = 20
        car.drive(100)
        self.assertEqual(car.fuel_amount, 10)


if __name__ == "__main__":
    unittest.main()
