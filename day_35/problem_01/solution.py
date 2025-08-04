def is_motion_detected(frame1, frame2):
    if frame1 != frame2:
        return True
    else:
        return False

frame1 = "empty"
frame2 = "person"

result = is_motion_detected(frame1, frame2)
print(result)

result2 = is_motion_detected("empty", "empty")
print(result2)