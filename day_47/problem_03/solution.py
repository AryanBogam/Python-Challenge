subject = "You won a lottery!"

banned_words = ["lottery", "win", "prize"]

is_spam = False
for word in banned_words:
    if word in subject.lower():
        is_spam = True

if is_spam:
    print("Spam")
else:
    print("Not Spam")