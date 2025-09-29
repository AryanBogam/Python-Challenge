def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Check length (2-6 characters)
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Rule 2: Must start with at least 2 letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    # Rule 5: Check for invalid characters (only letters and numbers allowed)
    if not s.isalnum():
        return False
    
    # Rules 3 & 4: Check number placement and first digit
    found_number = False
    for i, char in enumerate(s):
        if char.isdigit():
            # Rule 4: First number cannot be '0'
            if not found_number and char == '0':
                return False
            found_number = True
        else:
            # Rule 3: Once numbers start, can't have letters after
            if found_number:
                return False
    
    return True


if __name__ == "__main__":
    main()