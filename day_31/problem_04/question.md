Q4. Meeting Room Booking Conflicts
Problem: You manage a meeting room booking system.

Task:
Input: time slots in format ("09:00", "10:30")
Check if any slots overlap
Output: True if there’s conflict, else False

Sort by start time, then check if end time > next start time.