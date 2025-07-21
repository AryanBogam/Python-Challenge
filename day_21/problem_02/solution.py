def update_green_time(lane_id, emergency_detected, current_green_time):
    if emergency_detected:
        new_time = int(current_green_time * 1.5)
    else:
        new_time = current_green_time
    return {"lane_id": lane_id, "updated_green_time": new_time}

print(update_green_time("Lane-1", True, 60))
