def snap_score(sent, received):
    total = sent + received
    return total

sent = 1240
received = 876
result = snap_score(sent, received)
print(result)

result2 = snap_score(500, 750)
print(result2)