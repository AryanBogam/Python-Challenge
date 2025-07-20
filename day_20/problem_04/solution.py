import re
def is_suspicious_review(review):
    banned_words = ["scam", "fake", "terrible"]
    if any(word in review.lower() for word in banned_words):
        return True
    if review.count("😂") > 5:
        return True
    if re.search(r"(.)\1{4,}", review):
        return True
    return False

print(is_suspicious_review("Scam app 😂😂😂😂😂😂 do not download!!!!!"))
