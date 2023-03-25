class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):

    def test_initialization(self):
        worker = Worker("John Doe", 200, 10)
        self.assertEqual(worker.name, "John Doe")
        self.assertEqual(worker.salary, 200)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_rest(self):
        worker = Worker("John Doe", 200, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_work_with_zero_energy(self):
        worker = Worker("John Doe", 200, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_work_with_negative_energy(self):
        worker = Worker("John Doe", 200, -1)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_work_increase_money(self):
        worker = Worker("John Doe", 200, 10)
        worker.work()
        self.assertEqual(worker.money, 200)

    def test_work_decrease_energy(self):
        worker = Worker("John Doe", 200, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info_returns_correct_string(self):
        worker = Worker("John Doe", 200, 10)
        self.assertEqual(worker.get_info(), 'John Doe has saved 0 money.')

    # def setUp(self) -> None:
    #     self.worker = Worker("John Doe", 200, 1)
    #
    # def test_initialization(self):
    #     self.assertEqual(self.worker.name, "John Doe")
    #     self.assertEqual(self.worker.salary, 200)
    #     self.assertEqual(self.worker.energy, 1)
    #     self.assertEqual(self.worker.money, 0)
    #
    # def test_rest(self):
    #     self.worker.rest()
    #     self.assertEqual(self.worker.energy, 2)
    #
    # def test_work_with_zero_energy(self):
    #     with self.assertRaises(Exception) as context:
    #         self.worker.work()
    #         self.worker.work()
    #     self.assertEqual(str(context.exception), 'Not enough energy.')
    #
    # def test_work_with_negative_energy(self):
    #     with self.assertRaises(Exception) as context:
    #         self.worker.energy = 0
    #         self.worker.work()
    #     self.assertEqual(str(context.exception), 'Not enough energy.')
    #
    # def test_correct_salary_increased(self):
    #     self.worker.work()
    #     self.assertEqual(self.worker.salary, 200)
    #
    # def test_energy_decreased(self):
    #     self.worker.work()
    #     self.assertEqual(self.worker.energy, 0)
    #
    # def test_get_info_returns_correct_string(self):
    #     result = self.worker.get_info()
    #     self.assertEqual(result, f'John Doe has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
