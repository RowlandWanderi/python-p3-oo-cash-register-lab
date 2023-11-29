#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0
        
    def add_item(self,title,price,quantity=1):
      for item in range(quantity):
        self.items.append(title)
      self.total += price * quantity
      self.last_transaction = price * quantity
      
    def apply_discount(self):
      if self.discount == 0:
        print("There is no discount to apply.")
      else:
        self.total = round(self.total-(self.total * (self.discount/100)))
        print(f"After the discount, the total comes to ${self.total}.")
    
    def void_last_transaction(self):
      if len(self.items)>0 and self.last_transaction>0:
        self.total -= self.last_transaction
      elif len(self.items) == 0:
        self.total = 0