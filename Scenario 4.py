class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price > 50000:
            return "Premium"
        elif self.price > 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Category:", self.category())
        print()


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display_all(self):
        for mobile in self.mobiles:
            mobile.display()


# Create store
store = Store()

# Add mobiles
store.add_mobile(Mobile("Samsung", "S24", 80000))
store.add_mobile(Mobile("Redmi", "Note 13", 18000))
store.add_mobile(Mobile("OnePlus", "Nord", 30000))

# Display all mobiles
store.display_all()