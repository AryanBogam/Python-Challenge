user_input = input("Greeting: ").lower().replace(" ","")

if user_input.startswith("hello"):
    print("$0")
    
elif user_input.startswith("h"):
    print("$20")

elif ("h") in user_input:
    print("$100") 