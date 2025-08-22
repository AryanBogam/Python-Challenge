tags = ["#fun", "#sun", "#fun"]

unique_tags = []
for tag in tags:
    if tag not in unique_tags:
        unique_tags.append(tag)

print(unique_tags)