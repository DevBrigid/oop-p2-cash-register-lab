#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # One optional argument, default to 0
        self.discount = discount
        # Initialize total to zero
        self.total = 0.0
        # Initialize items to an empty list
        self.items = []
        # Internal log to track each transaction for the void feature
        self._last_transactions = []

    def add_item(self, title, price, quantity=1):
        # Calculate cost for this item line
        item_cost = price * quantity
        self.total += item_cost
        
        # Add the item title to the items list multiple times based on quantity
        for _ in range(quantity):
            self.items.append(title)
            
        # Log this specific event so we can perfectly reverse it if voided
        self._last_transactions.append({"title": title, "cost": item_cost, "quantity": quantity})

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # Apply percentage discount (e.g., 20 means 20% off, so multiply by 0.80)
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Ensure total converts nicely to an integer if it lands on a whole number like 800
            if self.total == int(self.total):
                self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if self._last_transactions:
            # Pop the most recent add_item record
            last = self._last_transactions.pop()
            
            # Subtract the exact line cost from the total
            self.total -= last["cost"]
            
            # Remove the exact number of matching titles from the end of the items list
            for _ in range(last["quantity"]):
                if last["title"] in self.items:
                    self.items.remove(last["title"])
