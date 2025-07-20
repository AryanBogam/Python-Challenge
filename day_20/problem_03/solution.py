
def backup_scheduler(hours_since_last_backup, battery_percent, has_wifi, is_charging):
    # If backup is overdue (more than 24 hours)
    if hours_since_last_backup > 24:
        if battery_percent > 50 and has_wifi:
            return "Backup now - conditions are good"
        elif battery_percent <= 20:
            return "Postpone until charging - battery too low"
        elif not has_wifi:
            return "Postpone until WiFi available"
        else:
            return "Postpone until better conditions"
    
    # If backup is recent but charging and on WiFi
    elif is_charging and has_wifi and battery_percent > 80:
        return "Backup now - optimal conditions"
    
    else:
        return "No backup needed yet"

print("Testing iCloud Backup Scheduler:")

print(backup_scheduler(30, 80, True, False))