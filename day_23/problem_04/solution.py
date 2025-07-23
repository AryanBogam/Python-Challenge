# The given sets and info
Alice = {"reading", "swimming", "coding", "music"}
Bob = {"gaming", "coding", "music", "dancing"}
Charlie = {"reading", "gaming", "cooking", "music"}

# Finding the intersection between all three friends.
Three_friends_share = Alice & Bob & Charlie

# Printing the answer of 1st quesiton.
print(f"Hobbies shared by all three friends: {Three_friends_share}.")

only_alice_hobbies = Alice.difference(Bob.union(Charlie))
# Printing the answer of 2nd question.
print(f"Hobbies only Alice has: {only_alice_hobbies}")

# Finding the hobbies alice and bob share but charlie doesn't.
AsB = Alice & Bob
CsAB = Charlie & AsB
CsN = AsB ^ CsAB

# Printing the answer of 3rd question.
print(f"Hobbies Alice and Bob share but Charlie doesn't: {CsN}")