def count_emote_usage(messages, emote):
    count = 0
    for message in messages:
        if emote in message:
            count += 1
    return count

messages = ["Kappa", "GG", "Kappa"]
result = count_emote_usage(messages, "Kappa")
print(result)

messages2 = ["PogChamp", "nice", "PogChamp", "amazing", "PogChamp"]
result2 = count_emote_usage(messages2, "PogChamp")
print(result2)