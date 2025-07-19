# 🧠 Day 19 – Amazon-Based Python Logic Challenges 🛒💻

✅ **Topics Practiced**  
- Conditional logic and dynamic workflows  
- Custom function design for real use cases  
- E-commerce systems thinking (cart, orders, delivery, reviews)  
- Problem solving with product- and customer-centric logic  
- Clean input/output management for UI/backend  

---

## 🚀 What I Solved Today  

Tackled **10 Python problems based on Amazon’s real-world scenarios**, including:

- ✅ Product pricing calculator with tax  
- ✅ Cart total engine with discounts  
- ✅ Inventory status checker  
- ✅ Order tracking simulator  
- ✅ Estimated delivery engine  
- ✅ Product review analyzer  
- ✅ Coupon code validator  
- ✅ Search bar keyword filter  
- ✅ Amazon Prime vs Non-Prime sorter  
- ✅ Return & refund condition checker  

Each problem reflects the kind of logic used in **Amazon’s core systems** — from purchase flows to backend intelligence.

---

## 💡 Learning Reflection

Today felt like I was working inside a real e-commerce tech team.

These weren’t just Python exercises — they were **mini-Amazon features**. From pricing to returns, I had to:

- Think like a backend engineer serving millions of users  
- Write logic that feels intuitive for real customers  
- Validate edge cases like invalid input or system errors  
- Handle data in ways similar to what real Amazon devs do  

I pushed myself to write **clean, structured, and production-minded code**.

This day reminded me:  
**“To build tech empires, you must first think like their engineers.”**

---

## 🧪 Sample Code – Cart Total Engine  
```python
def calculate_cart_total(cart_items):
    total = 0
    for item in cart_items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        total += price * quantity
    return round(total, 2)

cart = [
    {"price": 299.99, "quantity": 1},
    {"price": 149.99, "quantity": 2}
]
print("Total:", calculate_cart_total(cart))
