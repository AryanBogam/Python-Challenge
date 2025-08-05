def shorten_title(title):
    if len(title) > 50:
        return title[:50] + "..."
    else:
        return title

title = "This is a very long video title that goes beyond limit"
result = shorten_title(title)
print(result)

title2 = "Short title"
result2 = shorten_title(title2)
print(result2)