# Given .
employees_with_access = {"Alice", "Bob", "Charlie", "David"}
employees_on_leave = {"Charlie"}
attempted_entry = {"Alice", "Eve", "Charlie", "Frank"}

# 1. People who have access AND are not on leave
active_employees = employees_with_access - employees_on_leave
granted_access = attempted_entry & active_employees

# 2. People who tried but are either on leave OR not employees
denied_access = attempted_entry - active_employees

# 3. People who are not even employees 
unauthorized = attempted_entry - employees_with_access
