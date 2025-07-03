# Creating a tuple with strings  in it.
string_tuple = ("Hello", "World", "Python", "Programming", "Code")

# Finding longest string
longest_string = max(string_tuple, key=len)

# Finding  shortest string
shortest_string = min(string_tuple, key=len)

# Concatenating all strings
concatenated = " ".join(string_tuple)

# Final answers.
print(f"Original tuple: {string_tuple}")
print(f"Longest string: {longest_string} (length: {len(longest_string)})")
print(f"Shortest string: {shortest_string} (length: {len(shortest_string)})")
print(f"Concatenated string: {concatenated}")