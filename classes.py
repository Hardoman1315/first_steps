import abc


class ForgeItem(abc.ABC):
    def __init__ (self, forgingTime: float, amount: int):
        self.forgingTime : float = forgingTime
        self.amount : int = amount
        ForgeItem.totalForged = amount

    def totalTime(self) -> str:
        return f'Forging will take {self.forgingTime * self.amount} hours of forgingTime'

    @abc.abstractmethod
    def resources(self):
        pass

    @staticmethod
    def totalForgedCount():
        return ForgeItem.totalForged


class Materials(ForgeItem):
    def __init__(self, forgingTime: float, amount: int, cost: float, material: float):
        super().__init__(forgingTime, amount)
        self.cost : float = cost
        self.material : float= material
        self.totalMaterials : float = self.material * self.amount
        self.totalCurrencies : float = self.cost * self.amount

    def resources(self):
        return f'Required {self.totalMaterials} material and {self.totalCurrencies} currencies'


class AvailableMaterials(Materials):
    def __init__(self, forgingTime: float, amount: int, cost: float, material: float, availableCurrencies: float, availableMaterial: float):
        super().__init__(forgingTime, amount, cost, material)
        self.__availableCurrencies : float = availableCurrencies
        self._availableMaterial : float = availableMaterial

    def PossibilityOfForge(self) -> str:
        if self.__availableCurrencies < self.totalCurrencies or self._availableMaterial < self.totalMaterials:
            return 'Not enough resources to forge new item'
        else:
            return 'Sufficient resources to forge new item'


forgingTime = float(input("Enter forging forgingTime: "))
amount = int(input("Enter amount of forging: "))
cost = float(input("Enter cost of single forging: "))
material = float(input("Enter required amount of material to forge: "))
availableCurrencies = float(input("Enter available amount of currencies: "))
availableMaterial = float(input("Enter available amount of material: "))

available = AvailableMaterials(forgingTime, amount, cost, material, availableCurrencies, availableMaterial)

print(available.totalTime())
print(available.resources())
print(available.PossibilityOfForge())
