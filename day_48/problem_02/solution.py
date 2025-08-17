slides = [{"title": "Intro"}, {"title": ""}, {"title": "Conclusion"}]

result = []
for slide in slides:
    if slide["title"] == "":
        result.append("Missing Title")
    else:
        result.append(slide["title"])

print(result)