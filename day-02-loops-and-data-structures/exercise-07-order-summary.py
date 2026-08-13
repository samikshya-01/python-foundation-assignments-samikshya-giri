"""
Exercise 7: Nested Order Summary
Work with a dictionary of orders, where each order is itself
a dictionary containing customer, amount, and status.
"""

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. Print every order ID and customer
print("All orders:")
for order_id, details in orders.items():
    print(f"{order_id}: {details['customer']}")

# 2. Print only completed orders
print("\nCompleted orders:")
for order_id, details in orders.items():
    if details["status"] == "Completed":
        print(f"{order_id}: {details['customer']} - {details['amount']}")

# 3. Total amount of completed orders
completed_total = sum(
    details["amount"] for details in orders.values() if details["status"] == "Completed"
)
print("\nTotal completed amount:", completed_total)

# 4. Count pending orders
pending_count = sum(1 for details in orders.values() if details["status"] == "Pending")
print("Pending orders:", pending_count)

# 5. Add a new order
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 1200,
    "status": "Pending"
}
print("\nUpdated orders:", orders)