'''temp test file for models.py'''

from models import Customer, Food, ItemCategory, Transaction





#First Case: Vegan Female Customer
customer1 = Customer(1, "Priscilla")

itemCat1 = ItemCategory(1, "Main Course")

food1 = Food(1, "Vegan Wrap", 9.99, itemCat1, 4.5)

transaction1 = Transaction(1, customer1)
transaction1.add_item(food1)
print(f" \n First Case: \n")
print(" "* 5 + transaction1.get_transaction_details())
print(f" \n")


#Second Case: Carbs Lover Non-Binary Customer
customer2 = Customer(2, "Alex")
itemCat2 = ItemCategory(2, "Desserts")
food2 = Food(2, "Chocolate Cake", 5.99, itemCat2, 4.8)
transaction2 = Transaction(2, customer2)
transaction2.add_item(food2)
print(f" \n Second Case: \n")
print(" "* 5 + transaction2.get_transaction_details())
print(f" \n")


#Third Case: Caffeine Addict Male Customer
customer3 = Customer(3, "Michael")
itemCat3 = ItemCategory(3, "Beverages")
food3 = Food(3, "Espresso", 3.99, itemCat3, 4.9)
transaction3 = Transaction(3, customer3)
transaction3.add_item(food3)
print(f" \n Third Case: \n")
print(" "* 5 + transaction3.get_transaction_details())
print(f" \n")