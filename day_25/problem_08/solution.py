class SeatAlreadyTakenError(Exception):
    pass

def book_seat(booked_seats, seat):
    if seat in booked_seats:
        raise SeatAlreadyTakenError()

booked_seats = ["1A", "2B", "3C"]
seat = input("Enter seat: ")

try:
    book_seat(booked_seats, seat)
    print("Seat booked!")
except SeatAlreadyTakenError:
    print("Seat already taken!")