# Taking input of sleep hours and do they touch phone.
sleep = int(input("How many hours did you sleep: "))
phone = input("Did you touch your phone before sleep? (yes/no): ")

# It is condition to print.
if sleep > 7 and phone == "no":
    print("You're well rested and focused")

else:
    print("Fix your sleep habits!")