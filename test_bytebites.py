from models import Customer, Food, ItemCategory, Transaction, Menu

'''Logic Tests'''

#1. Total Cost Calculation Test

#1a. Test One Item
customer1 = Customer(1, "Priscilla")    
itemCat1 = ItemCategory(1, "Main Course")
food1 = Food(1, "Vegan Wrap", 9.99, itemCat1)
transaction1 = Transaction(1, customer1)
transaction1.add_item(food1)    

assertValue = 9.99
calculatedTotal = transaction1.calculate_total_cost()
assert calculatedTotal == assertValue, f"Expected total {assertValue}, but got {calculatedTotal}"

#1b. Test of the Same Items
itemCat2 = ItemCategory(2, "Desserts")
food2 = Food(2, "Chocolate Cake", 5.99, itemCat2)
transaction1.add_item(food2)
assertValue = 15.98
calculatedTotal = transaction1.calculate_total_cost()
assert calculatedTotal == assertValue, f"Expected total {assertValue}, but got {calculatedTotal}"


#1c. Test of Multiple Different Items
itemCat3 = ItemCategory(3, "Beverages")
food3 = Food(3, "Espresso", 3.99, itemCat3
transaction1.add_item(food3)
assertValue = 19.97
calculatedTotal = transaction1.calculate_total_cost()
assert calculatedTotal == assertValue, f"Expected total {assertValue}, but got {calculatedTotal}"   


print("Total Cost Calculation Test Passed")


#2. Category Filtering Test
menu = Menu()
menu.add_food_item(food1)
menu.add_food_item(food2)
menu.add_food_item(food3)

#add more asian fusion food to the current 3 catgories
food4 = Food(4, "Sushi Roll", 12.99, itemCat1)
menu.add_food_item(food4)
food5 = Food(5, "Mochi Ice Cream", 4.99, itemCat2)
menu.add_food_item(food5)
food6 = Food(6, "Green Tea Latte", 4.50, itemCat3)
menu.add_food_item(food6)
food7= Food(7, "Ramen Bowl", 14.99, itemCat1)
menu.add_food_item(food7)
food8= Food(8, "Honey Walnut Shrimp", 13.99, itemCat1)
menu.add_food_item(food8)


filtered_dessert_items = menu.get_foods_by_category("Desserts")
assert len(filtered_dessert_items) == 1, f"Expected 1 item in 'Desserts' category, but got {len(filtered_dessert_items)}"
assert filtered_dessert_items[0].name == "Chocolate Cake", f"Expected 'Chocolate Cake', but got {filtered_dessert   _items[0].name}"   

filtered_main_course_items = menu.get_foods_by_category("Main Course")
assert len(filtered_main_course_items) == 4, f"Expected 4 items in 'Main Course' category, but got {len(filtered_main_course_items)}"
main_course_names = [item.name for item in filtered_main_course_items]
expected_main_course_names = ["Vegan Wrap", "Sushi Roll", "Ramen Bowl", "Honey Walnut Shrimp"]
assert all(name in main_course_names for name in expected_main_course_names), f"Expected main
    course items {expected_main_course_names}, but got {main_course_names}"

filtered_beverage_items = menu.get_foods_by_category("Beverages")
assert len(filtered_beverage_items) == 2, f"Expected 2 items in 'Beverages' category, but got {len(filtered_beverage_items)}"
beverage_names = [item.name for item in filtered_beverage_items]
expected_beverage_names = ["Espresso", "Green Tea Latte"]
assert all(name in beverage_names for name in expected_beverage_names), f"Expected beverage items
    {expected_beverage_names}, but got {beverage_names}"

print("Category Filtering Test Passed")

#3. Purchase History Updates
customer2 = Customer(2, "Deven")
#check that purchase history is empty before adding transaction
transaction2 = Transaction(2, customer2, date=datetime(2026, 3, 2))
transaction2.add_item(food1)
transaction2.add_item(food2)
assert len(customer2.purchase_history) == 0, f"Expected purchase history to be empty, but got {len(customer2.purchase_history)} transactions"
customer2.purchase_history.append(transaction2)
assert len(customer2.purchase_history) == 2, f"Expected purchase history to have 2 transactions, but got {len(customer2.purchase_history)}"
assert customer2.purchase_history[0].transaction_id == 2, f"Expected transaction ID 2, but got {customer2.purchase_history[0].transaction_id}"
assert customer2.purchase_history[0].total_cost == 15.98, f"Expected total cost 15.98, but got {customer2.purchase_history[0].total_cost}"


#check total number of transactions in purchase history
transaction3 = Transaction(3, customer2, date=datetime(2026, 3, 3))
transaction3.add_item(food3)
customer2.purchase_history.append(transaction3)
assert len(customer2.purchase_history) == 3, f"Expected purchase history to have 3ctransactions, but got {len(customer2.purchase_history)}"
assert customer2.purchase_history[1].transaction_id == 3, f"Expected transaction ID 3, but got {customer2.purchase_history[1].transaction_id}"
assert customer2.purchase_history[1].total_cost == 3.99, f"Expected total cost 3.99, but got {customer2.purchase_history[1].total_cost}"

#check chronological order of transactions in purchase history
#add another transaction with a later date
transaction4 = Transaction(4, customer2, date=datetime(2026, 3, 4))
transaction4.add_item(food4)
customer2.purchase_history.append(transaction4)
assert len(customer2.purchase_history) == 4, f"Expected purchase history to have 4 transactions, but got {len(customer2.purchase_history)}"
assert customer2.purchase_history[2].transaction_id == 4, f"Expected transaction ID 4, but got {customer2.purchase_history[2].transaction_id}"
assert customer2.purchase_history[2].total_cost == 12.99, f"Expected total cost 12.99, but got {customer2.purchase_history[2].total_cost}"



#check multiple customers don't interfere with each other's purchase history
customer3 = Customer(3, "Emily")
transaction5 = Transaction(5, customer3, date=datetime(2026, 3, 2))
transaction5.add_item(food5)
customer3.purchase_history.append(transaction5)
assert len(customer3.purchase_history) == 1, f"Expected purchase history to have 1 transaction, but got {len(customer3.purchase_history)}"
assert customer3.purchase_history[0].transaction_id == 5, f"Expected transaction ID 5, but got {customer3.purchase_history[0].transaction_id}"
assert customer3.purchase_history[0].total_cost == 4.99, f"Expected total cost 4.99, but got {customer3.purchase_history[0].total_cost}"
assert len(customer2.purchase_history) == 4, f"Expected customer2's purchase history to still have 4 transactions, but got {len(customer2.purchase_history)}"





print("Purchase History Updates Test Passed")


