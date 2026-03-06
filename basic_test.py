'''temp test file for models.py'''

from models import Customer, Food, ItemCategory, Transaction, Menu





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


#Fourth Case: test Menu Item Category Management
itemCat4 = ItemCategory(4, "Salads")
food4 = Food(4, "Caesar Salad", 7.99, itemCat4, 4.2)
food5 = Food(5, "Angus Beef Steak", 21.99, itemCat1, 4.3)
food6 = Food(6, "Lemonade", 2.99, itemCat3, 4.0)
menu = Menu()

lst_of_categories = [food1, food2, food3, food4, food5, food6]
for food in lst_of_categories:
    menu.add_food_item(food)

print(f" \n Fourth Case: \n")
print(" "* 5 + "List All Food Items in Menu:")   
for food in menu.food_items:
    print(" "* 10 + food.get_details())

print(f" \n Fifth Case: \n")
print(" "* 5 + "Foods in 'Main Course' Category:")
for food in menu.get_foods_by_category("Main Course"):
    print(" "* 10 + food.get_details())

print(f" \n Sixth Case: \n")
print(" "* 5 + "Foods in 'Beverages' Category:")
for food in menu.get_foods_by_category("Beverages"):
    print(" "* 10 + food.get_details())