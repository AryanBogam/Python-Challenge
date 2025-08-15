def check_availability(booked_dates, requested_date):
    if requested_date in booked_dates:
        return "Not Available"
    else:
        return "Available"
    
booked_dates = ["2025-08-14", "2025-08-15"]
requested_date = "2025-08-16"
result = check_availability(booked_dates, requested_date)
print(result)

print(check_availability(booked_dates, "2025-08-14"))
print(check_availability(booked_dates, "2025-08-17"))
print(check_availability(["2025-08-10", "2025-08-11"], "2025-08-12"))