# Taking text as user input and with use of lower() converting capital letter to smaller letter.
text = input("Enter text: ").lower()

vowels = "aeiou"
for i in text:
    if i in vowels:
        print(i, end=" ")
