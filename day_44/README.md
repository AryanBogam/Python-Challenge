# 🐍 Day 44/300 – Azure Logic Systems in Python

Today, I built the **core logic behind Azure’s cloud services** — from validating blob storage names to calculating VM costs and checking service health.

It felt like simulating **Azure backend operations** in Python, breaking down how cloud systems validate, calculate, and monitor resources.

This day was **fun yet practical** — many tasks directly mirror what cloud engineers do daily when building on Azure.

---

## ✅ Topics Practiced

- 📂 Blob storage naming rules  
- 💰 VM cost calculation  
- 🏷️ Resource tag searching  
- 🌍 Region validation  
- 📦 Storage capacity checks  
- ⚡ Function trigger simulation  
- 🔐 IP whitelist verification  
- 📊 Deployment progress tracking  
- 🩺 Service health checks  
- 🚨 Cost alert notifications  

---

## 🔍 What I Solved Today

1. **Azure Storage Blob Name Checker**  
   → Validated file names against Azure’s blob naming rules.

2. **Azure VM Price Calculator**  
   → Calculated VM cost based on size and hours used.

3. **Azure Resource Tag Finder**  
   → Checked if a resource tag exists in a dictionary.

4. **Azure Region Validator**  
   → Verified if a given region is supported.

5. **Azure Storage Capacity Checker**  
   → Checked if adding new data would exceed storage limits.

6. **Azure Function Trigger Simulator**  
   → Simulated function execution based on trigger type.

7. **Azure IP Whitelist Check**  
   → Checked if an IP address is allowed access.

8. **Azure Deployment Status Tracker**  
   → Simulated a deployment progress display.

9. **Azure Service Health Checker**  
   → Returned the status (Running/Down) of a service.

10. **Azure Cost Alert**  
    → Triggered alerts when monthly costs exceeded budget.

---

## 💭 Daily Reflection

Today’s challenge gave me a **hands-on taste of cloud engineering logic**.  
Azure isn’t just about flashy dashboards — it’s **logic, rules, and validation** under the hood.

By simulating these features in Python, I’ve started thinking like a **cloud solutions architect**, focusing on both accuracy and efficiency.

Tomorrow? Pushing further into **real-world system simulations**.  
Because **“The systems you build today are the empires you run tomorrow.”**

---

## 🧠 Sample – Azure VM Price Calculator

```python
def calculate_vm_cost(size, hours):
    rates = {"B1": 0.02, "B2": 0.05, "B4": 0.10}
    if size in rates:
        return rates[size] * hours
    else:
        return "Invalid VM size"

# Example:
print(calculate_vm_cost("B2", 10))
# Output: 0.5
```
