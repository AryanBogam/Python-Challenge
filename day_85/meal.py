def main():
    time = input("What time is it? ")
    time, timing = convert(time)

    if 7 <= time < 8 and timing != "pm":
        print("breakfast time")
    elif 12 <= time < 13 and timing != "am":
        print("lunch time")
    elif 6 <= time < 7 and timing != "am":
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes,timing = minutes.split(" ")

    hours = int(hours)
    minutes = int(minutes)
    minutes = minutes / 60
    time = hours + minutes

    return time, timing

if __name__ == "__main__":
    main()