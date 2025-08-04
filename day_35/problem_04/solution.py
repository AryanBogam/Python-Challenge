def rotate_camera(angle):
    try:
        if angle < 0 or angle > 360:
            raise ValueError("Invalid angle")
        print(f"Rotating to angle {angle}°")
    except ValueError:
        print("Error: Invalid angle")

rotate_camera(90)
rotate_camera(380)
rotate_camera(-10)