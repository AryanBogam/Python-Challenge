votes = ["A","B","A","C","A","B"]

vote_count = {}
for vote in votes:
    if vote in vote_count:
        vote_count[vote] = vote_count[vote] + 1
    else:
        vote_count[vote] = 1

max_votes = 0
winner = ""
for candidate in vote_count:
    if vote_count[candidate] > max_votes:
        max_votes = vote_count[candidate]
        winner = candidate

print(winner)