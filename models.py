"""
Summary of 4 Classes

1. Customer - Has Name and Purchase History of Orders
2. FoodItem - Has name, price, category, popularityRating
3. Menu - Has a list of FoodItems and a method for filtering food by category
4. Order - Has a list of selected FoodItems and a method for calculating the total price

"""

from typing import Optional


class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        pass


class Menu:
    def __init__(self, items: Optional[list[FoodItem]] = None):
        pass
        

    def filter_by_category(self, category: str) -> list[FoodItem]:
        return []


class Order:
    def __init__(self, selected_items: Optional[list[FoodItem]] = None):

    def add_item(self, item: FoodItem) -> None:
        pass

    def compute_total_cost(self) -> float:
        return 0.0


class Customer:
    def __init__(self, name: str, purchase_history: Optional[list[Order]] = None):
        pass
      

    def verify_user(self) -> bool:
        return False
