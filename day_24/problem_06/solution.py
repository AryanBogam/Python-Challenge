poll = {
    "Python": 0,
    "Java": 0,
    "JavaScript": 0,
    "C++": 0
}

voted_users = set()

votes = [
    ("user1", "Python"),
    ("user2", "Java"),
    ("user3", "Python"),
    ("user1", "Java"),
    ("user4", "JavaScript")
]

print("Processing votes:")
for user, choice in votes:
    if user in voted_users:
        print(f"{user} already voted - prevented double voting")
    else:
        if choice in poll:
            poll[choice] = poll[choice] + 1
            voted_users.add(user)
            print(f"{user} voted for {choice}")

print("\nPoll Results:")
for option, votes in poll.items():
    print(f"{option}: {votes} votes")

winner = ""
max_votes = 0
for option, votes in poll.items():
    if votes > max_votes:
        max_votes = votes
        winner = option

print(f"\nWinner: {winner} with {max_votes} votes")