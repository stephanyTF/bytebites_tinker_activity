import unittest

from models import FoodItem, Order, Menu


class TestOrderBehavior(unittest.TestCase):
    def test_calculate_total_with_multiple_items(self):
        # Happy path: total should equal the sum of item prices
        burger = FoodItem("Burger", 10.00, "Main Course", 4.0)
        soda = FoodItem("Soda", 5.00, "Beverage", 3.0)
        menu = Menu([burger, soda])

        order = Order()
        order.add_item(burger)
        order.add_item(soda)

        self.assertEqual(order.compute_total_cost(), 15.00)

        # Category filtering + sorting behavior
        main_course_items = menu.filter_by_category("Main Course")
        self.assertEqual(main_course_items, [burger])

        sorted_items = sorted(menu.items, key=lambda item: item.price)
        self.assertEqual(sorted_items, [soda, burger])

    def test_order_total_is_zero_when_empty(self):
        # Edge case: an order with no items should total $0, not crash
        order = Order()

        self.assertEqual(order.compute_total_cost(), 0)

    def test_add_item_not_in_menu(self):
        # Edge case: current behavior accepts items not on the menu (no validation yet)
        burger = FoodItem("Burger", 10.00, "Main Course", 4.0)
        soda = FoodItem("Soda", 5.00, "Beverage", 3.0)
        menu = Menu([burger, soda])

        mystery_item = FoodItem("Mystery Item", 99.00, "Unknown", 0.0)
        self.assertNotIn(mystery_item, menu.items)

        order = Order()
        order.add_item(mystery_item)

        self.assertIn(mystery_item, order.selected_items)
        self.assertEqual(order.compute_total_cost(), 99.00)


if __name__ == "__main__":
    unittest.main()
