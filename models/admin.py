from .user import User, Role

class Admin(User):
    def __init__(self, username):
        super().__init__(username, Role.ADMIN)

    def add_product(self, store, name, price, stock):
        store.add_product(name, price, stock)
        