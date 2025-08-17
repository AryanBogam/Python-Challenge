slides = ["Intro", "Agenda", "Conclusion"]

temp = slides[0]
slides[0] = slides[2]
slides[2] = temp

print(slides)