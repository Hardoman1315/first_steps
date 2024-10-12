import abc
import random


class ForgeItem(abc.ABC):
    def __init__(self, forgingTime: float, amount: int):
        self.forgingTime : float = forgingTime
        self.amount : int = amount
        ForgeItem.totalForged : int = 0

    def totalTime(self) -> str:
        return f'Forging will take {self.forgingTime * self.amount} hours of forgingTime'

    @abc.abstractmethod
    def resources(self):
        pass

    @staticmethod
    def totalForgedCount(self) -> float:
        for _ in range(amount: int):
            ForgeItem.totalForged += 1


class Materials(ForgeItem):
    def __init__(self, forgingTime: float, amount: int, cost: float, material: float):
        super().__init__(forgingTime, amount)
        self.cost : float = cost
        self.material : float= material
        self.totalMaterials : float = self.material * self.amount
        self.totalCurrencies : float = self.cost * self.amount

    def discount(self) -> str:
        if self.amount >= 5:
            self.totalMaterials = self.totalMaterials * 0.9
            return f'Discount for forging multiple items is 10% and total amount of required materials - {self.totalMaterials}'
        else:
            return 'Not enough items in forge to get discount'

    def resources(self):
        return f'Required {self.totalMaterials} material and {self.totalCurrencies} currencies'


class AvailableMaterials(Materials):
    def __init__(self, forgingTime: float, amount: int, cost: float, material: float, availableCurrencies: float, availableMaterial: float):
        super().__init__(forgingTime, amount, cost, material)
        self.__availableCurrencies : float = availableCurrencies
        self._availableMaterial : float = availableMaterial

    def getAvailableMaterial(self) -> float:
        return self._availableMaterial

    def setAvailableMaterial(self) -> str:
        self._availableMaterial = AvailableMaterial
        return f'AvailableMaterial now equal {self._availableMaterial}'

    @property
    def getAvailableCurrencies(self) -> float:
        return self.__availableCurrencies

    @getAvailableCurrencies.setter
    def getAvailableCurrencies(self, availableCurrencies: float):
        self.__availableCurrencies = availableCurrencies

    def possibilityOfForge(self) -> str:
        if self.__availableCurrencies < self.totalCurrencies or self._availableMaterial < self.totalMaterials:
            return 'Not enough resources to forge new item'
        else:
            return 'Sufficient resources to forge new item'


# Uncomment to manual input

"""
forgingTime = float(input("Enter forging forgingTime: "))
amount = int(input("Enter amount of forging: "))
cost = float(input("Enter cost of single forging: "))
material = float(input("Enter required amount of material to forge: "))
availableCurrencies = float(input("Enter available amount of currencies: "))
availableMaterial = float(input("Enter available amount of material: "))
"""

# Comment to random input

forgingTime = random.uniform(1, 10)
amount = random.randint(1, 10)
cost = random.uniform(1, 10)
material = random.uniform(1, 10)
availableCurrencies = random.uniform(1, 100)
availableMaterial = random.uniform(1, 100)

available = AvailableMaterials(forgingTime, amount, cost, material, availableCurrencies, availableMaterial)

print(available.totalTime())
print(available.resources())
print(available.discount())
print(available.possibilityOfForge())
