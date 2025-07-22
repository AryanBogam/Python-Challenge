def check_conflict(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    if distance < 5:
        print("Risk of collision")
    else:
        print("Safe distance")

check_conflict(10, 20, 12, 23)

check_conflict(10, 20, 20, 30)
