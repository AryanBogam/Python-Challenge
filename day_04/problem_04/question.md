 Question 4: Access Control Logic – Office Entry System
 
Scenario: You have three sets:
Employees with access: {"Alice", "Bob", "Charlie", "David"}
Employees on leave: {"Charlie"}
People who attempted entry: {"Alice", "Eve", "Charlie", "Frank"}

Determine:
Who should be granted access?
Who should be denied (on leave or not an employee)?
Who are unauthorized outsiders?

Expected Logic:
Use intersection() to find valid access
Use difference() to identify non-employees and leave status
Think like you're building an office door entry AI system

