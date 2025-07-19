from datetime import datetime, timedelta

order_date = input("Enter order date (YYYY-MM-DD): ")
delivery_days = int(input("Estimated delivery days: "))

order_dt = datetime.strptime(order_date, "%Y-%m-%d")
delivery_dt = order_dt + timedelta(days=delivery_days)

print(f"Estimated Delivery Date: {delivery_dt.date()}")