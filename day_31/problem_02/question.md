Q2. Shift Scheduler for Factory Workers
Problem: Assign 3 shifts (Morning, Evening, Night) to workers based on day of week.

Task:
Input: list of worker names, current day
Output: shift schedule (e.g., rotating logic like shift A -> B -> C)
Prevent same person getting same shift 2 days in a row

Try using modulo logic and tracking previous shifts.