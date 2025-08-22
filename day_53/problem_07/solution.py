upload_time = 10
current_time = 12

time_passed = current_time - upload_time

if time_passed >= 24:
    print("Expired")
else:
    print("Not expired")