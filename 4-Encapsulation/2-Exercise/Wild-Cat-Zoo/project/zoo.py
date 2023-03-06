from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget - price < 0:
            return "Not enough budget"

        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return f"Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_salaries = sum(map(lambda w: w.salary, self.workers))

        if self.__budget - total_salaries < 0:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_cost = sum(map(lambda a: a.money_for_care, self.animals))

        if self.__budget - animals_cost < 0:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))

        result = [f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:"]
        result.extend(lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(str(r) for r in result)

    def workers_status(self):
        keepers = list(filter(lambda w: w.__class__.__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda w: w.__class__.__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda w: w.__class__.__name__ == "Vet", self.workers))

        result = [f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:"]
        result.extend(keepers)

        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(str(r) for r in result)
