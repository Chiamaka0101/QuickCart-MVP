class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, amount):
        self.stock += amount

    def reduce_stock(self, qty):
        if qty <= self.stock:
            self.stock -= qty
            return True
        return False

    def __str__(self):
        return f"{self.name} (${self.price}, stock={self.stock})"