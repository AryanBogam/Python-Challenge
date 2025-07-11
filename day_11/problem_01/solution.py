def format_string(text):
    # Remove punctuation and lower the text
    import string
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    # Replace space with dash
    return text.replace(" ", "-")

print(format_string("Hello, World!"))
