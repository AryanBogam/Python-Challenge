orders = {
    "A001": "Shipped",
    "A002": "Out for Delivery",
    "A003": "Delivered",
    "A004": "Cancelled"
}

def track_order(order_id):
    return orders.get(order_id, "Invalid Order ID")

print(track_order("A003"))
