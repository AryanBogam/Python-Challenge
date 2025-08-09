def highest_viewer_count(viewer_counts):
    highest = 0
    for count in viewer_counts:
        if count > highest:
            highest = count
    return highest

viewer_counts = [120, 150, 180, 160]
result = highest_viewer_count(viewer_counts)
print(result)

viewer_counts2 = [95, 120, 89, 145, 200]
result2 = highest_viewer_count(viewer_counts2)
print(result2)