class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([(title, price)] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_title, last_item_price = self.items.pop()
            self.total -= last_item_price
        else:
            print("No transactions to void.")

# Testing the CashRegister class
test_register = CashRegister(20)
test_register.add_item("eggs", 1.99)
test_register.add_item("tomato", 1.76)
print(test_register.items)  # Output should be [('eggs', 1.99), ('tomato', 1.76)]
test_register.void_last_transaction()
print(test_register.total)  # Output should be 1.99
