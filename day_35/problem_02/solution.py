def check_cameras(status_list):
    working = 0
    not_working = 0
    
    for status in status_list:
        if status == "on":
            working += 1
        else:
            not_working += 1
    
    print(f"Working: {working}, Not working: {not_working}")

status_list = ["on", "off", "on", "off", "on"]
check_cameras(status_list)