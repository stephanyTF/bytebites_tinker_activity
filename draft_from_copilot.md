classDiagram
    class Customer {
        -customerId: int
        -name: string
        -purchaseHistory: Transaction[]
        +getCustomerId() int
        +getName() string
        +addTransaction(transaction: Transaction) void
        +getPurchaseHistory() Transaction[]
    }
    
    class Food {
        -foodId: int
        -name: string
        -price: double
        -category: ItemCategory
        -popularityRating: double
        +getFoodId() int
        +getName() string
        +getPrice() double
        +getCategory() ItemCategory
        +getPopularityRating() double
        +setPopularityRating(rating: double) void
    }
    
    class ItemCategory {
        -categoryId: int
        -categoryName: string
        +getCategoryId() int
        +getCategoryName() string
    }
    
    class Transaction {
        -transactionId: int
        -customer: Customer
        -items: Food[]
        -totalCost: double
        +getTransactionId() int
        +getCustomer() Customer
        +getItems() Food[]
        +addItem(food: Food) void
        +calculateTotalCost() double
        +getTotalCost() double
    }
    
    Customer "1" --> "*" Transaction : has
    Transaction "*" --> "*" Food : contains
    Food "*" --> "1" ItemCategory : belongs to