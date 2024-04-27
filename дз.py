class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"{self.name} - Price: ${self.price}, Availability: {self.availability}"


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity=1):
        if product.availability >= quantity:
            self.items.append((product, quantity))
            product.availability -= quantity
            print(f"{quantity} {product.name}(s) added to cart.")
        else:
            print("Insufficient stock!")

    def remove_from_cart(self, product, quantity=1):
        for item in self.items:
            if item[0] == product:
                if item[1] > quantity:
                    item[1] -= quantity
                    product.availability += quantity
                    print(f"{quantity} {product.name}(s) removed from cart.")
                else:
                    self.items.remove(item)
                    product.availability += item[1]
                    print(f"All {product.name}(s) removed from cart.")
                return
        print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total

    def checkout(self):
        total = self.calculate_total()
        print(f"Total amount to pay: ${total}")
        self.items = []
        print("Thank you for shopping with us!")