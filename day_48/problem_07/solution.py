slide = {"title": "Project Plan", 
         "bullets": ["Timeline details", "Budget estimation"]}

title_words = slide["title"].split()
total_words = len(title_words)

for bullet in slide["bullets"]:
    bullet_words = bullet.split()
    total_words = total_words + len(bullet_words)

print(total_words)