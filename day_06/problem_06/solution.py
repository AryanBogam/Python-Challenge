# Taking input of speed.
speed = int(input("Enter your download speed (Mbps): "))

# Condition to print.
if speed >= 100:
    print("Streaming god")
elif speed >= 50:
    print("Fast enough")
else:
    print("Go cry to your ISP")
