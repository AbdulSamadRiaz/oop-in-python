
class User:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Customer(User):

    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self.address = address

    def display_info(self):
        print(f"Customer: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")


class Restaurant:

    def __init__(self, restaurant_name, location):
        self.restaurant_name = restaurant_name
        self.location = location


class FoodItem:

    def __init__(self, food_name, price):
        self.food_name = food_name
        self.price = price

    def display_info(self):
        print(f"{self.food_name}: {self.price}")


class Order:

    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, food):
        self.items.append(food)
        print(f"{food.food_name} added to order.")

    def calculate_total(self):
        total = 0

        for food in self.items:
            total += food.price

        print(f"Total Order Amount: {total}")


# Create customer
customer1 = Customer("Abdul Samad Riaz", "07896", "Karachi")

# Create food items
food1 = FoodItem("Biryani", 500)
food2 = FoodItem("Burger", 800)

# Create order
order1 = Order(customer1)

# Add food items
order1.add_item(food1)
order1.add_item(food2)

# Calculate total
order1.calculate_total()
