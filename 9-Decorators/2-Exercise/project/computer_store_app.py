from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        self.warehouse.append(computer)

        return computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price <= client_budget and wanted_processor == comp.processor and comp.ram >= wanted_ram:
                self.profits += client_budget - comp.price
                self.warehouse.remove(comp)

                return f"{comp} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
