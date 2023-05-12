import csv

class Item:

    all = []
    pay_rate = 0.8 # After 20% discount
    def __init__(self,name: str,price: float,quantity: int) -> None:

        assert price >= 0, f"Price {price} invalid!"
        assert quantity >= 0, f"Quantity {quantity} invalid!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod            
    def instantiate_values_csv(cls, file_path):
        with open(file_path,'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name',''),
                price=float(item.get('price', 0.0)),
                quantity=int(item.get('quantity', 0)),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        return isinstance(num,int)

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
Item.instantiate_values_csv("/home/amritesh/Personal/OOPS/items.csv")
print(Item.is_integer(7.6))