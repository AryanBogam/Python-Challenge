numbers = []

print("Enter numbers (type 'done' to finish):")

while True:
    user_input = input("Enter number: ")
    if user_input == "done":
        break
    numbers.append(int(user_input))

if numbers:
    max_num = max(numbers)
    min_num = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    print("Statistics:")
    print("Max:", max_num)
    print("Min:", min_num)
    print("Sum:", total)
    print("Average:", average)
else:
    print("No numbers entered!")