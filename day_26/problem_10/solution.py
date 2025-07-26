import random

while True:
    number = random.randint(1000, 9999)
    print(f"Generated: {number}")
    
    # Checking if it ends in 777
    if number % 1000 == 777:
        print(f"Lucky number found: {number}")
        break