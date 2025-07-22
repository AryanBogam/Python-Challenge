code = input("Enter flight code (e.g. AI202): ").strip()

if len(code) == 5 and code[:2].isalpha() and code[:2].isupper() and code[2:].isdigit():
    print("Valid flight code")
else:
    print("Invalid flight code")
