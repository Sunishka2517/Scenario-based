class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def category(self):
        if self.price > 1000:
            return "Expensive"
        else:
            return "Affordable"

    def display(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category())
        print()


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all(self):
        for product in self.products:
            product.display()


# Create inventory
inventory = Inventory()

# Add products
inventory.add_product(Product(101, "Laptop", 50000))
inventory.add_product(Product(102, "Mouse", 800))
inventory.add_product(Product(103, "Keyboard", 1500))

# Display all products
inventory.display_all()