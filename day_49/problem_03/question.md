Q3. Mute/Unmute
Task: Simulate mute/unmute toggle.
If muted, sound = 0; if unmuted, restore previous volume.
Input:
previous_volume = 60, muted = True
Output: 0  
Input:
previous_volume = 60, muted = False
Output: 60
Why: VLC stores your previous volume when you unmute.