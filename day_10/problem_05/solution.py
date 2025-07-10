# Given string
sentence = "  python is powerful  "

# Remove the whitespaces from the right and left and title  
sentence = sentence.strip()
print(sentence.title())  # Capitalize each word

# Count 'o'
print("Count of 'o':", sentence.count("o"))
