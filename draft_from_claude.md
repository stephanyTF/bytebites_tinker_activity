┌─────────────────────────────┐
│          Customer           │
├─────────────────────────────┤
│ - name: String              │
│ - purchaseHistory: List      │
├─────────────────────────────┤
│ + isVerifiedUser(): Boolean  │
│ + getPurchaseHistory(): List  │
└──────────────┬──────────────┘
               │ places
               │ 1..*
               ▼
┌─────────────────────────────┐
│         Transaction         │
├─────────────────────────────┤
│ - items: List<Food>         │
│ - totalCost: Float          │
├─────────────────────────────┤
│ + addItem(food: Food): void  │
│ + computeTotal(): Float      │
└──────────────┬──────────────┘
               │ contains
               │ 1..*
               ▼
┌─────────────────────────────┐
│            Food             │
├─────────────────────────────┤
│ - name: String              │
│ - price: Float              │
│ - popularityRating: Float   │
│ - category: ItemCategory    │
├─────────────────────────────┤
│ + getDetails(): String      │
└──────────────┬──────────────┘
               │ belongs to
               │ *..1
               ▼
┌─────────────────────────────┐
│        ItemCategory         │
├─────────────────────────────┤
│ - categoryName: String      │
│ - items: List<Food>         │
├─────────────────────────────┤
│ + filterByCategory(): List   │
│ + addItem(food: Food): void  │
└─────────────────────────────┘
