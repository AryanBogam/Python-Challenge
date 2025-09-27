def main():
    # Get input from user
    text = input("Input: ")
    
    # Remove vowels and print result
    result = shorten(text)
    print("Output:", result)


def shorten(word):
    # Define vowels to remove (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Build result string without vowels
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    
    return result


if __name__ == "__main__":
    main()