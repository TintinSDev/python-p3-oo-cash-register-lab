#!/usr/bin/env python3


class CashRegister:

  def __init__(self, discount = 0):
    
 
    
    self.discount = discount
    self.total = 0
    self.items = []
    self.track_subtotal = []
 
  
  def add_item(self, title, price, quantity=1):
      self.title = title
      self.price = price
      self.quantity = quantity 
      
      self.total += quantity*price
      
      self.track_subtotal.append(price*quantity)

    
      for _ in range(quantity):
        self.items.append(title)

      return self.total
  
  
  def apply_discount(self):
    if self.discount > 0:
        discount_amount = (self.discount / 100) * self.total
        print(f"Discount amount: {discount_amount}")
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${self.total:.2f}.")
    else:
        print("There is no discount to apply.")

    
  def void_last_transaction(self):
    self.total -= self.track_subtotal[-1]
    return self.total



new_register = CashRegister()
new_register.add_item("eggs", 1.99, 2)
new_register.add_item("tomato", 1.76, 3)
print(new_register.items)
    