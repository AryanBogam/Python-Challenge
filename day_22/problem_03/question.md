Q3. Emergency Priority Queue
Problem:
You have a list of flights waiting to land. Each flight has a priority:

Normal: 1

Emergency: 2
Write a program that prints the flight queue such that emergencies land first, then normal flights.
queue = [["AI101", 1], ["EK303", 2], ["BA205", 1]]

Output:
EK303
AI101
BA205

 Hint: Sort list manually based on priority without using sort().