from models.product import Product

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, stock):
        self.products.append(Product(name, price, stock))

    def list_products(self):
        return [str(p) for p in self.products]

    def find_product(self, name):
        for p in self.products:
            if p.name == name:
                return p
        return None