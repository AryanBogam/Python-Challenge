portfolio = 10000
every_month = 5000

months = 0
while portfolio < 100000:
    portfolio += every_month
    months += 1

print(f"You became a crypto whale in {months} months!")