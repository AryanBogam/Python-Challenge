Add 
update
delete
view
exit# Student Grades Management System - Building Logic

## 🤔 **Step 1: Think First - What do we need?**

Before writing any code, ask yourself:
- What information do I need to store? → **Student Name + Grade**
- Where will I store it? → **Dictionary (like a phone book)**
- What actions can users do? → **Add, Update, Delete, View**

---

## 📝 **Step 2: Plan on Paper**

### What the user should be able to do:
1. **Add** a new student with their grade
2. **Update** an existing student's grade
3. **Delete** a student
4. **View** all students
5. **Exit** the program

### Flow Chart (Mental Picture):
```
Start → Show Menu → Get User Choice → Do Action → Back to Menu → Repeat
```

---

## 🏗️ **Step 3: Build Step by Step**

### **3.1 First - Storage**
```
Think: "I need a place to store data"
Solution: Create an empty dictionary
```

### **3.2 Second - Basic Operations**
Think about each operation one by one:

**For Adding:**
- Get name from user
- Get grade from user  
- Store in dictionary
- Tell user "Done!"

**For Updating:**
- Get name from user
- Check: Does this student exist?
  - If YES → Update grade
  - If NO → Tell user "Not found"

**For Deleting:**
- Get name from user
- Check: Does this student exist?
  - If YES → Remove from dictionary
  - If NO → Tell user "Not found"

**For Viewing:**
- Check: Any students stored?
  - If YES → Show all students
  - If NO → Tell user "Empty"

### **3.3 Third - Menu System**
```
Think: "User needs options to choose from"
Solution: Loop + Menu + User Input
```

---

## 🎯 **Step 4: The Building Order**

### **Build in this exact order:**

1. **Create storage** (dictionary)
2. **Write one function at a time:**
   - Start with `add_student()` - easiest
   - Then `display_all_students()` - to see if add worked
   - Then `update_student()` - similar to add
   - Then `delete_student()` - similar to update
3. **Create the menu** (main function)
4. **Connect everything** together

---

## 💡 **Step 5: Key Programming Concepts**

### **Dictionary Logic:**
```
Think of it like a real dictionary:
- Word = Student Name (Key)
- Meaning = Grade (Value)
```

### **Input/Output Logic:**
- **Input:** What user gives us
- **Process:** What we do with it
- **Output:** What we show back

### **Error Handling:**
Always ask: "What if user enters wrong thing?"
- Student doesn't exist?
- Invalid menu choice?

---

## 🚀 **Step 6: Test Your Logic**

### **Before coding, trace through manually:**

**Example Flow:**
1. User chooses "Add Student"
2. User enters "John" and "85"
3. Dictionary becomes: `{"John": 85}`
4. Show success message
5. Back to menu

**Test Edge Cases:**
- What if dictionary is empty?
- What if user tries to update non-existent student?
- What if user enters invalid menu choice?

