classDiagram
    class Customer {
        -String name
        -List~Order~ purchaseHistory
        +verifyUser() bool
    }

    class FoodItem {
        -String name
        -double price
        -String category
        -double popularityRating
    }

    class Menu {
        -List~FoodItem~ items
        +filterByCategory(category) List~FoodItem~
        +add_item(item)
    }

    class Order {
        -List~FoodItem~ selectedItems
        +add_item(item)
        +computeTotalCost() double
    }

    Customer "1" --> "many" Order : places
    Menu "1" *-- "many" FoodItem : contains
    Order "1" *-- "many" FoodItem : contains
