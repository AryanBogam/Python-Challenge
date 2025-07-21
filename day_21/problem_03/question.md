Q3. Violation Tracker System
Detect how many times vehicles jumped red light in a session.

Input: List of violations like:
[{"vehicle": "MH12AB1234", "time": "10:05", "light": "red"}, ...]

Output: Dictionary of vehicles with their total violations. If any has > 3, flag it.