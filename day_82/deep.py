user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Check all valid forms of 42
if user_input == "42":
    print("Yes")
elif user_input == "forty-two":
    print("Yes")
elif user_input == "Forty Two":
    print("Yes")
else:
    print("No")