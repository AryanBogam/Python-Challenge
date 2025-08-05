def filter_comment(comment):
    banned_words = ["spam", "scam", "fake"]
    
    for word in banned_words:
        if word in comment.lower():
            return "Blocked"
    return "Approved"

comment = "This video is a scam!"
result = filter_comment(comment)
print(result)

comment2 = "Great video!"
result2 = filter_comment(comment2)
print(result2)