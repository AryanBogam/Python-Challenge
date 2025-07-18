months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

while True:
    date = input("Enter date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                break

        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month.isalpha():
                month = month.lower()
                if month in months:
                    month = months[month]
                    day = int(day)
                    year = int(year)
                    if 1 <= month <= 12 and 1 <= day <= 31:
                        break
    except:
        continue

print(f"{year:04}-{month:02}-{day:02}")
