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
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f}\n)"


class Menu:
    def __init__(self, items: Optional[list[FoodItem]] = None):
        self.items = items if items is not None else []

    def filter_by_category(self, category: str) -> list[FoodItem]:
        filtered_items = [item for item in self.items if item.category == category]
        return filtered_items


class Order:
    def __init__(self, selected_items: Optional[list[FoodItem]] = None):
        self.selected_items = selected_items if selected_items is not None else []

    def add_item(self, item: FoodItem) -> None:
        self.selected_items.append(item)

    def compute_total_cost(self) -> float:
        return sum(item.price for item in self.selected_items)

    def __repr__(self):
        return f"{self.selected_items}"


class Customer:
    def __init__(self, name: str, purchase_history: Optional[list[Order]] = None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def verify_user(self) -> bool:
        #ensure name is not empty (purchase history can be empty for new users)
        return self.name.strip() != ""


#Temporary Script
if __name__ == "__main__":
    # Create some food items
    pizza = FoodItem("Pizza", 10.99, "Main Course", 4.5)
    burger = FoodItem("Burger", 8.99, "Main Course", 4.0)
    salad = FoodItem("Salad", 6.99, "Appetizer", 3.5)

    # Create a menu and add food items
    menu = Menu([pizza, burger, salad])

    # Filter food items by category
    main_course_items = menu.filter_by_category("Main Course")
    print("Main Course Items:")
    for item in main_course_items:
        print(f"- {item.name}: ${item.price}")

    # Create an order and add selected items
    order = Order()
    order.add_item(pizza)
    order.add_item(salad)

    # Compute total cost of the order
    total_cost = order.compute_total_cost()
    print(f"\nTotal Cost of Order: ${total_cost:.2f}")

    # Create a customer with their order and verify user
    customer = Customer("Jaq Roe", [order])
    is_verified = customer.verify_user()

    #Add order to customer's purchase history
    print(f"\nIs Customer Verified? {'Yes' if is_verified else 'No'}")
    print(f"Customer Name: {customer.name}")
    print(f"Purchase History: {len(customer.purchase_history)} order(s):\n {customer.purchase_history}")