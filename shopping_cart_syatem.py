
class ShoppingCart:

    def __init__(self):
        self.items = []

    # Add product to cart
    def add_item(self, name, price):

        if price <= 0:
            print("Invalid product price!")
            return

        product = {
            "name": name,
            "price": price
        }

        self.items.append(product)
        print(name, "product added successfully!")

    # Remove product from cart
    def remove_cart(self, name):

        for item in self.items:

            if item["name"] == name:
                self.items.remove(item)
                print(name, "removed successfully!")
                return

        print("Product not found!")

    # Display all products
    def display_products(self):

        print("\n======== Shopping Cart ========")

        if not self.items:
            print("Your shopping cart is empty!")
            return

        for item in self.items:
            print(f"Product: {item['name']}")
            print(f"Price: {item['price']}")

    # Calculate total and discount
    def calculate_total(self):

        total = 0

        for item in self.items:
            total += item["price"]

        print("\nSubtotal:", total)

        if total > 10000:

            discount = total * 0.10
            total = total - discount

            print("Discount: 10%")
            print("Total discount:", discount)

        else:
            print("No discount applied!")

        print("Final total:", total)

    # Count products
    def count_items(self):
        print("Total products:", len(self.items))

    # Clear cart
    def clear_cart(self):
        self.items.clear()
        print("Shopping cart cleared!")


# Create shopping cart object
cart1 = ShoppingCart()

# Add products
cart1.add_item("Mobile", 50000)
cart1.add_item("Charger", 5000)
cart1.add_item("Bag", 500)

# Display products
cart1.display_products()

# Remove product
cart1.remove_cart("Bag")

# Calculate total
cart1.calculate_total()

# Count products
cart1.count_items()
