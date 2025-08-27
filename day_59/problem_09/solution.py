import random

lottery_numbers = set()

while len(lottery_numbers) < 5:
    number = random.randint(1, 50)
    lottery_numbers.add(number)

print("Your lottery ticket numbers:")
for number in sorted(lottery_numbers):
    print(number)