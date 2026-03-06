from datetime import datetime


class Customer:
    """Manages customer information and purchase history."""
    
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.purchase_history = []
    
    def add_transaction(self, transaction):
        """Adds a transaction to the customer's purchase history."""
        self.purchase_history.append(transaction)
    
    def get_purchase_history(self):
        """Returns all transactions for this customer."""
        return self.purchase_history
    
    def get_customer_info(self):
        """Returns formatted customer information."""
        return f"Customer: {self.name} (ID: {self.customer_id})"


class ItemCategory:
    """Manages food item categories."""
    
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
        self.food_items = []
    
    def add_food_item(self, food):
        """Adds a food item to this category."""
        self.food_items.append(food)
    
    def remove_food_item(self, food):
        """Removes a food item from this category."""
        if food in self.food_items:
            self.food_items.remove(food)
    
    def get_foods_in_category(self):
        """Returns all food items in this category."""
        return self.food_items
    
    def get_category_name(self):
        """Returns the category name."""
        return self.category_name


class Food:
    """Represents a food item on the menu."""
    
    def __init__(self, food_id, name, price, category, popularity_rating=0.0):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating
    
    # Note: Not in UML but saved in case needed for future functionality
    # #def update_price(self, new_price):
    #     """Updates the price of this food item."""
    #     self.price = new_price
    
    def get_details(self):
        """Returns formatted food item information."""
        return f"{self.name} - ${self.price:.2f} (Rating: {self.popularity_rating}/5) [Category: {self.category.get_category_name()}]"
    

    def set_rating(self, rating):
        """Updates the popularity rating for this food item."""
        self.popularity_rating = rating



class Menu:
    """A list that holds all items and lets us filter by category such as "Drinks" or "Desserts"."""
    def __init__(self):
        self.food_items = []
    
    def add_food_item(self, food):
        """Adds a food item to the menu."""
        self.food_items.append(food)
    
    
    def get_foods_by_category(self, category_name):
        """Returns all food items in a specific category."""
        return [food for food in self.food_items if food.category.get_category_name() == category_name]
    
    def get_all_foods(self):
        """Returns all food items on the menu."""
        return self.food_items


class Transaction:
    """Represents a customer purchase transaction."""
    
    def __init__(self, transaction_id, customer, date=None):
        self.transaction_id = transaction_id
        self.customer = customer
        self.items = []
        self.timestamp = date if date else datetime.now()
        self.total_cost = 0.0
    
    def add_item(self, food):
        """Adds a food item to this transaction and updates total cost."""
        self.items.append(food)
        self.calculate_total_cost()
    
    def remove_item(self, food):
        """Removes a food item from this transaction and updates total cost."""
        if food in self.items:
            self.items.remove(food)
            self.calculate_total_cost()
    
    def calculate_total_cost(self):
        """Calculates and returns the total cost of all items in the transaction."""
        self.total_cost = sum(food.price for food in self.items)
        return self.total_cost
    
    def get_transaction_details(self):
        """Returns formatted transaction information."""
        items_str = ", ".join([food.name for food in self.items])
        return f"Transaction {self.transaction_id} - Customer: {self.customer.name} - Items: {items_str} - Total: ${self.total_cost:.2f} - Timestamp: {self.timestamp}"