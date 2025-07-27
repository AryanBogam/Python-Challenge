def reverse_string(text):
    try:
        return str(text)[::-1]
    except:
        return "Invalid input"

text = input("Enter text: ")
print(f"Reversed: {reverse_string(text)}")