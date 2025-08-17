slides = [{"title": "", "bullets": []},
          {"title": "Agenda", "bullets": ["Topic 1"]}]

result = []
for i in range(len(slides)):
    slide = slides[i]
    if slide["title"] == "" and len(slide["bullets"]) == 0:
        result.append("Slide " + str(i + 1) + " is empty")

print(result)