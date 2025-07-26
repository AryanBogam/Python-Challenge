while True:
    word = input("Enter word (or 'exit' to stop): ")
    
    if word.lower() == "exit":
        break

    if word == word[::-1]:
        print(f"'{word}' is a palindrome!")
    else:
        print(f"'{word}' is not a palindrome.")