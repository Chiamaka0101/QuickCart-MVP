# from models.admin import Admin
# from models.user import User, Role
# from models.rider import Rider
# from services.store import Store
# from services.order_services import OrderService

# def demo():
#     print("Running QuickCart demo mode (non-interactive)...\n")

#     # Setup store and services
#     store = Store()
#     orders = OrderService()

#     # Admin adds products
#     admin = Admin("superadmin")
#     admin.add_product(store, "Soda", 2.5, 10)
#     admin.add_product(store, "Chips", 7.0, 5)
#     print("[Admin adds products]")
#     print("Added Soda and Chips\n")

#     # User registers and places order
#     user = User("alice", Role.USER)
#     soda = store.find_product("Soda")
#     chips = store.find_product("Chips")

#     cart = [(soda, 1), (chips, 1)]
#     if all(p.reduce_stock(q) for p, q in cart):
#         order = orders.create_order(user, cart)
#         print("[User registers and places order]")
#         print(f"Order created by {user.username}, total ${order.total}, status {order.status}\n")

#     # Rider registers and accepts order
#     rider = Rider("bob")
#     rider.accept_order(order)
#     print("[Rider registers and accepts order]")
#     print(f"Order {order.id} assigned to rider {rider.username}, status {order.status}\n")

#     # Rider delivers order
#     rider.deliver_order(order)
#     print("[Rider delivers order]")
#     print(f"Order {order.id} final status: {order.status}")

# if __name__ == "__main__":
#     demo()


from models.admin import Admin
from models.user import User, Role
from models.rider import Rider
from services.store import Store
from services.order_services import OrderService

# --- Helper Functions ---
def admin_menu(admin, store, orders):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Product")
        print("2. Restock Product")
        print("3. View Products")
        print("4. View Orders")
        print("0. Logout")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Product name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            admin.add_product(store, name, price, stock)
            print(f"Added {name}")
        elif choice == "2":
            name = input("Product name to restock: ")
            product = store.find_product(name)
            if product:
                qty = int(input("Amount: "))
                product.restock(qty)
                print(f"Restocked {name}, new stock={product.stock}")
            else:
                print("Product not found.")
        elif choice == "3":
            print("Products:")
            for p in store.list_products():
                print(" -", p)
        elif choice == "4":
            print("Orders:")
            for o in orders.list_orders():
                print(" -", o)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def user_menu(user, store, orders):
    while True:
        print(f"\n--- User Menu ({user.username}) ---")
        print("1. Browse Products")
        print("2. Place Order")
        print("3. View My Orders")
        print("0. Logout")
        choice = input("Choose: ")

        if choice == "1":
            for p in store.list_products():
                print(" -", p)
        elif choice == "2":
            cart = []
            while True:
                name = input("Enter product name (or 'done'): ")
                if name.lower() == "done":
                    break
                product = store.find_product(name)
                if product:
                    qty = int(input("Quantity: "))
                    if product.reduce_stock(qty):
                        cart.append((product, qty))
                        print(f"Added {qty} x {product.name}")
                    else:
                        print("Not enough stock.")
                else:
                    print("Product not found.")
            if cart:
                order = orders.create_order(user, cart)
                print(f"Order created {order.id}, total ${order.total}, status {order.status}")
        elif choice == "3":
            for o in orders.orders:
                if o.user == user.username:
                    print(" -", o)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def rider_menu(rider, orders):
    while True:
        print(f"\n--- Rider Menu ({rider.username}) ---")
        print("1. View Pending Orders")
        print("2. Accept Order")
        print("3. Deliver Order")
        print("0. Logout")
        choice = input("Choose: ")

        if choice == "1":
            for o in orders.orders:
                if o.status == "Pending":
                    print(" -", o)
        elif choice == "2":
            oid = input("Enter order ID to accept: ")
            order = next((o for o in orders.orders if o.id == oid), None)
            if order:
                rider.accept_order(order)
                print(f"Order {oid} assigned to {rider.username}")
            else:
                print("Order not found.")
        elif choice == "3":
            oid = input("Enter order ID to deliver: ")
            order = next((o for o in orders.orders if o.id == oid), None)
            if order:
                rider.deliver_order(order)
                print(f"Order {oid} delivered.")
            else:
                print("Order not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


# --- Main App ---
def main():
    store = Store()
    orders = OrderService()

    print("=== Welcome to QuickCart ===")

    while True:
        print("\nChoose role:")
        print("1. Admin")
        print("2. User")
        print("3. Rider")
        print("0. Exit")
        role_choice = input("Select: ")

        if role_choice == "1":
            name = input("Enter admin name: ")
            admin = Admin(name)
            admin_menu(admin, store, orders)

        elif role_choice == "2":
            name = input("Enter username: ")
            user = User(name, Role.USER)
            user_menu(user, store, orders)

        elif role_choice == "3":
            name = input("Enter rider name: ")
            rider = Rider(name)
            rider_menu(rider, orders)

        elif role_choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()