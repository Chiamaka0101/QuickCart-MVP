from models.order import Order

class OrderService:
    def __init__(self):
        self.orders = []

    def create_order(self, user, cart):
        order = Order(user.username, cart)
        self.orders.append(order)
        return order

    def list_orders(self):
        return [str(o) for o in self.orders]