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
    }

    class Order {
        -List~FoodItem~ selectedItems
        +computeTotalCost() double
    }

    Customer "1" --> "many" Order : places
    Menu "1" *-- "many" FoodItem : contains
    Order "1" *-- "many" FoodItem : contains
