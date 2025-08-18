Q2. Volume Up/Down
Task: Given a current volume (0–100), increase or decrease it.
Clamp values so volume never goes below 0 or above 100.
Input:
volume = 95, change = +10
Output: 100
volume = 5, change = -10
Output: 0
Why: VLC prevents volume from exceeding limits.