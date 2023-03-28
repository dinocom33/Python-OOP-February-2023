from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(10, 200)

    def test_correct_initialization(self):
        self.assertEqual(self.vehicle.fuel, 10)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 200)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_without_enough_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(2)
        self.assertEqual(self.vehicle.fuel, 7.5)

    def test_refuel_with_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel_with_correct_capacity(self):
        self.vehicle.fuel = 5
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 10)

    def test__str__returns_correct_string(self):
        result = str(self.vehicle)
        self.assertEqual(result, "The vehicle has 200 " +
                         "horse power with 10 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    main()
