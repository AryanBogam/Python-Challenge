slides = [{"title": "Intro", "theme": "Dark"},
          {"title": "Agenda", "theme": "Dark"}]

first_theme = slides[0]["theme"]
same_theme = True

for slide in slides:
    if slide["theme"] != first_theme:
        same_theme = False

print(same_theme)