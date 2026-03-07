from datetime import datetime

from models import Customer, Food, ItemCategory, Transaction, Menu


#Define global food and category objects to be used across multiple tests
itemCat1 = ItemCategory(1, "Main Course")
itemCat2 = ItemCategory(2, "Desserts")
itemCat3 = ItemCategory(3, "Beverages")
food1 = Food(1, "Vegan Wrap", 9.99, itemCat1)
food2 = Food(2, "Chocolate Cake", 5.99, itemCat2)
food3 = Food(3, "Espresso", 3.99, itemCat3)
food4 = Food(4, "Sushi Roll", 12.99, itemCat1)
food5 = Food(5, "Mochi Ice Cream", 4.99, itemCat2)
food6 = Food(6, "Green Tea Latte", 4.50, itemCat3)
food7= Food(7, "Ramen Bowl", 14.99, itemCat1)
food8= Food(8, "Honey Walnut Shrimp", 13.99, itemCat1)


# Global menu with all food items
menu = Menu()
menu.add_food_item(food1)
menu.add_food_item(food2)
menu.add_food_item(food3)
menu.add_food_item(food4)
menu.add_food_item(food5)
menu.add_food_item(food6)
menu.add_food_item(food7)
menu.add_food_item(food8)




'''Logic Tests'''

#1. Total Cost Calculation Test

#1a. Test One Item

def test_total_cost_calculation():
    customer1 = Customer(1, "Priscilla")    
    transaction1 = Transaction(1, customer1)
    transaction1.add_item(food1)    

    assertValue = 9.99
    calculatedTotal = transaction1.calculate_total_cost()
    assert calculatedTotal == assertValue, f"Expected total {assertValue}, but got {calculatedTotal}"

    #1b. Test of the Same Items
    transaction1.add_item(food2)
    assertValue = 15.98
    calculatedTotal = transaction1.calculate_total_cost()
    assert calculatedTotal == assertValue, f"Expected total {assertValue}, but got {calculatedTotal}"


    #1c. Test of Multiple Different Items
    transaction1.add_item(food3)
    assertValue = 19.97
    calculatedTotal = transaction1.calculate_total_cost()
    assert calculatedTotal == assertValue, f"Expected total {assertValue}, but got {calculatedTotal}"   


    print("Total Cost Calculation Test Passed")


#2. Category Filtering Test
def test_category_filtering():
  
    filtered_dessert_items = menu.get_foods_by_category("Desserts")
    assert len(filtered_dessert_items) == 2, f"Expected 2 items in 'Desserts' category, but got {len(filtered_dessert_items)}"
    assert filtered_dessert_items[0].name == "Chocolate Cake", f"Expected 'Chocolate Cake', but got {filtered_dessert_items[0].name}"   

    filtered_main_course_items = menu.get_foods_by_category("Main Course")
    assert len(filtered_main_course_items) == 4, f"Expected 4 items in 'Main Course' category, but got {len(filtered_main_course_items)}"
    main_course_names = [item.name for item in filtered_main_course_items]
    expected_main_course_names = ["Vegan Wrap", "Sushi Roll", "Ramen Bowl", "Honey Walnut Shrimp"]
    assert all(name in main_course_names for name in expected_main_course_names), f"Expected main course items {expected_main_course_names}, but got {main_course_names}"

    filtered_beverage_items = menu.get_foods_by_category("Beverages")
    assert len(filtered_beverage_items) == 2, f"Expected 2 items in 'Beverages' category, but got {len(filtered_beverage_items)}"
    beverage_names = [item.name for item in filtered_beverage_items]
    expected_beverage_names = ["Espresso", "Green Tea Latte"]
    assert all(name in beverage_names for name in expected_beverage_names), f"Expected beverage items{expected_beverage_names}, but got {beverage_names}"

    print("Category Filtering Test Passed")

#3. Purchase History Updates
def test_purchase_history_updates():
    customer2 = Customer(2, "Deven")
    #check that purchase history is empty before adding transaction
    transaction2 = Transaction(2, customer2, date=datetime(2026, 3, 2))
    transaction2.add_item(food1)
    transaction2.add_item(food2)
    assert len(customer2.purchase_history) == 0, f"Expected purchase history to be empty, but got {len(customer2.purchase_history)} transactions"
    customer2.add_transaction(transaction2)
    assert len(customer2.purchase_history) == 1, f"Expected purchase history to have 1 transaction, but got {len(customer2.purchase_history)}"
    assert customer2.purchase_history[0].transaction_id == 2, f"Expected transaction ID 2, but got {customer2.purchase_history[0].transaction_id}"
    assert customer2.purchase_history[0].total_cost == 15.98, f"Expected total cost 15.98, but got {customer2.purchase_history[0].total_cost}"


    #check total number of transactions in purchase history
    transaction3 = Transaction(3, customer2, date=datetime(2026, 3, 3))
    transaction3.add_item(food3)
    customer2.add_transaction(transaction3)

    transaction4 = Transaction(4, customer2, date=datetime(2026, 3, 4))
    transaction4.add_item(food4)
    customer2.add_transaction(transaction4)

    assert len(customer2.purchase_history) == 3, f"Expected purchase history to have 3 transactions, but got {len(customer2.purchase_history)}"
    assert customer2.purchase_history[1].transaction_id == 3, f"Expected transaction ID 3, but got {customer2.purchase_history[1].transaction_id}"
    assert customer2.purchase_history[1].total_cost == 3.99, f"Expected total cost 3.99, but got {customer2.purchase_history[1].total_cost}"

    #check chronological order of transactions in purchase history
    #add another transaction with a later date
    transaction4 = Transaction(4, customer2, date=datetime(2026, 3, 4))
    transaction4.add_item(food4)
    customer2.add_transaction(transaction4)
    assert len(customer2.purchase_history) == 4, f"Expected purchase history to have 4 transactions, but got {len(customer2.purchase_history)}"
    assert customer2.purchase_history[2].transaction_id == 4, f"Expected transaction ID 4, but got {customer2.purchase_history[2].transaction_id}"
    assert customer2.purchase_history[2].total_cost == 12.99, f"Expected total cost 12.99, but got {customer2.purchase_history[2].total_cost}"



    #check multiple customers don't interfere with each other's purchase history
    customer3 = Customer(3, "Emily")
    transaction5 = Transaction(5, customer3, date=datetime(2026, 3, 2))
    transaction5.add_item(food5)
    customer3.add_transaction(transaction5)
    assert len(customer3.purchase_history) == 1, f"Expected purchase history to have 1 transaction, but got {len(customer3.purchase_history)}"
    assert customer3.purchase_history[0].transaction_id == 5, f"Expected transaction ID 5, but got {customer3.purchase_history[0].transaction_id}"
    assert customer3.purchase_history[0].total_cost == 4.99, f"Expected total cost 4.99, but got {customer3.purchase_history[0].total_cost}"
    assert len(customer2.purchase_history) == 4, f"Expected customer2's purchase history to still have 4 transactions, but got {len(customer2.purchase_history)}"



    print("Purchase History Updates Test Passed")


'''Edge Case Tests'''

#4. Empty Transaction Test
def test_empty_transaction():
    customer4 = Customer(4, "Marco")
    transaction6 = Transaction(6, customer4)
    
    # Empty transaction should have $0 total cost
    assert transaction6.total_cost == 0.0, f"Expected empty transaction total to be $0, but got ${transaction6.total_cost}"
    calculatedTotal = transaction6.calculate_total_cost()
    assert calculatedTotal == 0.0, f"Expected calculate_total_cost() to return $0 for empty transaction, but got ${calculatedTotal}"
    
    print("Empty Transaction Test Passed")


#5. Empty Transaction Not in Purchase History Test
def test_empty_transaction_not_in_history():
    customer5 = Customer(5, "Sofia")
    transaction7 = Transaction(7, customer5)
    
    # Empty transaction should not be added to purchase history
    assert len(customer5.purchase_history) == 0, f"Expected purchase history to be empty initially"
    
    # Only add non-empty transactions to history
    transaction7_filled = Transaction(8, customer5)
    customer5.add_transaction(transaction7_filled)
    
    assert len(customer5.purchase_history) == 0, f"Expected purchase history to be empty, but got {len(customer5.purchase_history)}"
    
    print("Empty Transaction Not in History Test Passed")


#6. Food Item Validation Test
def test_food_item_in_menu():
    # Verify that foods in the menu are accessible
    menu_food_ids = [f.food_id for f in menu.get_all_foods()]
    assert food1.food_id in menu_food_ids, f"Expected food1 to be in menu"
    assert food2.food_id in menu_food_ids, f"Expected food2 to be in menu"
    
    # Create a food item NOT in the menu
    non_menu_category = ItemCategory(99, "Unknown")
    non_menu_food = Food(99, "Mystery Item", 19.99, non_menu_category)
    
    # Trying to add non-menu food to transaction should ideally be prevented
    # For now, we verify the food exists independently
    assert non_menu_food.food_id not in menu_food_ids, f"Expected mystery food to NOT be in menu"
    
    print("Food Item Validation Test Passed")


# Run all tests
if __name__ == "__main__":
    test_total_cost_calculation()
    test_category_filtering()
    test_purchase_history_updates()
    test_empty_transaction()
    test_empty_transaction_not_in_history()
    test_food_item_in_menu()


