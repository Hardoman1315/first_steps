import abc
import random


class ForgeItem(abc.ABC):
    total_forged : int = 0
    def __init__(self, forging_time: float, amount: int):
        self.forging_time : float = forging_time
        self.amount : int = amount

    def total_time(self) -> str:
        return f'Forging will take {self.forging_time * self.amount} hours of forging_time'

    @abc.abstractmethod
    def resources(self):
        pass

    @staticmethod
    def total_forged_count(amount) -> int:
        for _ in range(amount):
            ForgeItem.total_forged += 1
        return ForgeItem.total_forged


class Materials(ForgeItem):
    def __init__(self, forging_time: float, amount: int, cost: float, material: float):
        super().__init__(forging_time, amount)
        self.cost : float = cost
        self.material : float = material
        self.total_materials : float = self.material * self.amount
        self.total_currencies : float = self.cost * self.amount

    def discount(self) -> str:
        if self.amount >= 5:
            self.total_materials = self.total_materials * 0.9
            return (
                f"Discount for forging multiple items is 10% "
                f"and total amount of required materials - {self.total_materials}"
            )
        else:
            return 'Not enough items in forge to get discount'

    def resources(self):
        return f'Required {self.total_materials} material and {self.total_currencies} currencies'


class AvailableMaterials(Materials):
    def __init__(self, forging_time: float, amount: int, cost: float, material: float,
                available_currencies: float, available_materials: float):
        super().__init__(forging_time, amount, cost, material)
        self.__available_currencies : float = available_currencies
        self._available_materials : float = available_materials

    def get_available_material(self) -> float:
        return self._available_materials

    def set_available_material(self, available_materials: float) -> str:
        self._available_materials = available_materials
        return f'Available material now equal {self._available_materials}'

    @property
    def get_available_currencies(self) -> float:
        return self.__available_currencies

    @get_available_currencies.setter
    def get_available_currencies(self, available_currencies: float):
        self.__available_currencies = available_currencies
        print(f'Available currencies now equal {self.__available_currencies}')

    def possibility_of_forge(self) -> str:
        if (self.__available_currencies < self.total_currencies or
            self._available_materials < self.total_materials):
            return 'Not enough resources to forge new item'
        else:
            return 'Sufficient resources to forge new item'


# Uncomment to manual input

# forging_time = float(input("Enter forging forging_time: "))
# amount = int(input("Enter amount of forging: "))
# cost = float(input("Enter cost of single forging: "))
# material = float(input("Enter required amount of material to forge: "))
# available_currencies = float(input("Enter available amount of currencies: "))
# available_materials = float(input("Enter available amount of material: "))


# Uncomment to random input

forging_time = random.uniform(1, 10)
amount = random.randint(1, 10)
cost = random.uniform(1, 10)
material = random.uniform(1, 10)
available_currencies = random.uniform(1, 100)
available_materials = random.uniform(1, 100)
available = AvailableMaterials(forging_time, amount, cost, material,
                               available_currencies, available_materials)

print(available.total_time())
print(available.resources())
print(available.discount())
print(available.get_available_material())
print(available.set_available_material(80))
available.get_available_currencies = 80
print(available.possibility_of_forge())
