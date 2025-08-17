slides = ["Intro", "Agenda", "Intro", "Conclusion"]

duplicates = []
for i in range(len(slides)):
    for j in range(i + 1, len(slides)):
        if slides[i] == slides[j]:
            if slides[i] not in duplicates:
                duplicates.append(slides[i])

print(duplicates)