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
    ''' The Customer class is defined by name and ID and has a purchase history of their past transactions'''
    
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
    
        ''' The Food class is defined by name, ID, price, and category. '''


    class ItemCategory {
        -categoryId: int
        -categoryName: string
        +getCategoryId() int
        +getCategoryName() string
    }
        ''' The itemCategory class is defined by name and ID. Misses a list of foods that belong under its category'''



    
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
   ''' Each transaction has an id, belogns to one customer, contains a list of food, and lists total cost '''


    Customer "1" --> "*" Transaction : has
    Transaction "*" --> "*" Food : contains
    Food "*" --> "1" ItemCategory : belongs to