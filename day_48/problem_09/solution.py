slides = [{"title": "Intro", "bullets": ["Welcome"]},
          {"title": "Agenda", "bullets": ["Python basics"]}]
keyword = "Python"

result = []
for slide in slides:
    found = False
    if keyword in slide["title"]:
        found = True
    for bullet in slide["bullets"]:
        if keyword in bullet:
            found = True
    if found:
        result.append(slide["title"])

print(result)