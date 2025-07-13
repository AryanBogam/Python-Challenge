# 🧠 Day 13 – Input Validation & Exception Handling 🛡️

✅ **Topics Practiced**:  
try, except, else, finally, type casting, input validation, logic building, error handling, file access

---

---

### ✅ Problems Solved:
1. 🔞 Age validator with input and range checks  
2. ➗ Division calculator with zero and type handling  
3. 🧮 Even number checker with input validation  
4. 📧 Email format checker using `try-except`  
5. 🔍 Float vs Integer type identifier  
6. ✔️ Safe square root calculator with negative check  
7. 🔁 Retry-until-valid input loop using exception  
8. 🔐 4-digit pin validator  
9. 📦 List index access with out-of-bound error control  
10. 🧾 **Mini Project** – Validated Form (Name, Age, Email) with complete error handling  

---

## 🧪 Sample – Mini Validated Form (Question 10)
```python
def validate_form():
    try:
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be positive.")

        email = input("Enter your email: ").strip()
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")

    except ValueError as e:
        print("Form Error:", e)
    else:
        print("✅ Form submitted successfully!")
        print(f"Name: {name}, Age: {age}, Email: {email}")

validate_form()
