#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction_amount = transaction_amount
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount
            self.items.pop()
        else:
            print("No transactions to void.")
