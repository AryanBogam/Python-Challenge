# Contact Book App - Code Logic

## 🤔 **Think First**
What do we need?
- Store multiple contacts (Name + Details)
- Let user pick what to do
- Keep running until they say stop

---

## 📋 **The Plan**

### **Data Structure**
Use a **dictionary of dictionaries**:
```
contacts = {
    "John": {"age": 25, "email": "john@email.com", "mobile": "123456"},
    "Sarah": {"age": 30, "email": "sarah@email.com", "mobile": "789012"}
}
```

### **User Flow**
1. Show menu
2. Get choice
3. Do the thing
4. Repeat

---

## 🛠️ **Build Logic**

### **1. Storage Setup**
- Empty dictionary to start
- Will grow as user adds contacts

### **2. Menu System**
- Infinite loop (`while True`)
- Print options 1-7
- Get user input

### **3. Each Feature Logic**

**Create Contact:**
- Get name → Check if exists → Get details → Store

**View Contact:**
- Get name → Check if exists → Display details

**Update Contact:**
- Get name → Check if exists → Get new details → Replace

**Delete Contact:**
- Get name → Check if exists → Remove from dictionary

**Search Contact:**
- Get search term → Loop through all → Check if name matches → Display matches

**Count Contacts:**
- Use `len()` on dictionary

**Exit:**
- Print goodbye → `break` the loop

---

## 🎯 **Key Concepts**

### **Dictionary Operations**
- `name in contacts` → Check existence
- `contacts[name]` → Access/Store
- `del contacts[name]` → Delete
- `contacts.items()` → Loop through all

### **Error Prevention**
Always ask: "What if contact doesn't exist?"
- Check before viewing
- Check before updating  
- Check before deleting

### **User Experience**
- Clear menu options
- Helpful error messages
- Confirmation messages

---

## 🔄 **The Flow**

```
Start → Create Dictionary → Show Menu → Get Choice → 
Process Choice → Back to Menu → Repeat Until Exit
```

**Each choice follows pattern:**
1. Get user input
2. Validate (does contact exist?)
3. Do the action
4. Give feedback

---

## 💡 **Why This Works**

- **Dictionary** = Perfect for key-value storage (name → details)
- **Nested Dictionary** = Store multiple details per contact
- **Menu Loop** = Keeps program running
- **Validation** = Prevents crashes
- **Modular Thinking** = Each feature is separate

---

## 🚀 **Build Order**

1. Dictionary + Menu structure
2. Create contact (easiest)
3. View contact (test if create worked)
4. Update contact (similar to create)
5. Delete contact (simple dictionary operation)
6. Search + Count (more complex)
7. Exit + Error handling

**Remember:** Build one feature at a time, test it, then move to next! 