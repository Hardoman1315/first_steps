import abc

class ForgeItem(abc.ABC):
    def __init__ (self, time: int, amount: int):
        self.time = time
        self.amount = amount
        ForgeItem.totalForged = amount

    def totalTime(self) -> int:
        return f'Forging will take {self.time * self.amount} hours of time'

    @abc.abstractmethod
    def resources(self):
        pass

    @staticmethod
    def totalForgedCount():
        return ForgeItem.totalForged

class Materials(ForgeItem):
    def __init__ (self, time: int, amount: int, cost: int, material: int):
        super().__init__(time, amount)
        self.cost = cost
        self.material = material
        self.totalMaterials = self.material * self.amount
        self.totalCurrencies = self.cost * self.amount

    def resources(self):
        return f'Required {self.totalMaterials} material and {self.totalCurrencies} currencies'

class AvailableMaterials(Materials):
    def __init__ (self, time: int, amount: int, cost: int, material: int, availableCurrencies: int, availableMaterial: int):
        super().__init__(time, amount, cost, material)
        self.__availableCurrencies = availableCurrencies
        self._availableMaterial = availableMaterial

    def PossibilityOfForge(self) -> str:
        if self.__availableCurrencies < self.totalCurrencies or self._availableMaterial < self.totalMaterials:
            return 'Not enough resources to forge new item'
        else:
            return 'Sufficient resources to forge new item'

time = int(input("Enter forging time: "))
amount = int(input("Enter amount of forging: "))
cost = int(input("Enter cost of single forging: "))
material = int(input("Enter required amount of material to forge: "))
availableCurrencies = int(input("Enter available amount of currencies: "))
availableMaterial = int(input("Enter available amount of material: "))

available = AvailableMaterials(time, amount, cost, material, availableCurrencies, availableMaterial)

print(available.totalTime())
print(available.resources())
print(available.PossibilityOfForge())
