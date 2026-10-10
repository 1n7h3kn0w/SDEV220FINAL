from datetime import datetime

def GetTime() -> str:
    time = str(datetime.now().time()).split('.')[0]
    return time

class order:
    def __init__(self, customer: str, ToGo: bool, items: list, price: float):
        self.customer = customer
        self.ToGo = ToGo
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
    def __init__(self, ItemID: int, UnitPrice: float, Stock: int, TaxRate: float):
        self.ID = ItemID
        self.price = UnitPrice
        self.stock = Stock
        self.TaxRate
    
    def CalculatePrice(self, UnitsSold: int):
        return ((self.price * UnitsSold) * (1+self.TaxRate))