from datetime import datetime

def GetTime() -> str:
    time = str(datetime.now().time()).split('.')[0]
    return time

class order:
    def __init__(self, customer: str, items: list, price: float):
        self.customer = customer
        self.items = items
        self.price = price
        self.time = GetTime()
        self.open = True
    
    def close(self) -> None:
        self.open = False

class FoodItem:
    def __init__(self, name: str, UnitPrice: float, alterations: None | list):
        self.name = name
        self.price = UnitPrice
        self.alterations = alterations
        

class StoreItem:
    def __init__(self, ItemID: int, UnitPrice: float, Stock: int):
        self.ID = ItemID
        self.price = UnitPrice
        self.stock = Stock
    
    def CalculatePrice(self, UnitsSold: int, TaxRate: float):
        return ((self.price * UnitsSold) * (1+TaxRate))