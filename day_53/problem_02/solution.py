hashtags = ["#fun", "#sun", "#fun", "#python"]

count = {}
for tag in hashtags:
    if tag in count:
        count[tag] = count[tag] + 1
    else:
        count[tag] = 1

max_count = 0
top_tag = ""
for tag in count:
    if count[tag] > max_count:
        max_count = count[tag]
        top_tag = tag

print(top_tag)