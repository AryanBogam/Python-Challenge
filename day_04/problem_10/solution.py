# Given.
used_dark_mode = {"Aryan", "Om", "Tina", "Riya"}
used_voice_commands = {"Tina", "Riya", "Sahil"}
used_notifications = {"Aryan", "Om", "Meera", "Sahil"}

# 1.All three features
used_all = used_dark_mode & used_voice_commands & used_notifications

# Combine sets
all_users = used_dark_mode | used_voice_commands | used_notifications

# Exactly two features
dark_and_voice = used_dark_mode & used_voice_commands
dark_and_notif = used_dark_mode & used_notifications
voice_and_notif = used_voice_commands & used_notifications

used_two = (dark_and_voice | dark_and_notif | voice_and_notif) - used_all

# Only one feature
used_any_two_or_more = used_all | used_two
used_only_one = all_users - used_any_two_or_more
