import uuid

class Order:
    def __init__(self, user, items):
        self.id = str(uuid.uuid4())[:6]   # short readable ID
        self.user = user
        self.items = items  # list of (Product, qty)
        self.total = sum(p.price * q for p, q in items)
        self.status = "Pending"
        self.rider = None

    def assign(self, rider_name):
        if self.status == "Pending":
            self.status = "Assigned"
            self.rider = rider_name

    def deliver(self):
        if self.status == "Assigned":
            self.status = "Delivered"

    def __str__(self):
        return f"Order {self.id} by {self.user}, total ${self.total}, status {self.status}"
