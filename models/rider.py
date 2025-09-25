from .user import User, Role

class Rider(User):
    def __init__(self, username):
        super().__init__(username, Role.RIDER)

    def accept_order(self, order):
        if order.status == "Pending":
            order.assign(self.username)

    def deliver_order(self, order):
        if order.status == "Assigned" and order.rider == self.username:
            order.deliver()