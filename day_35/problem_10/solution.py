def count_people(events):
    count = 0
    for event in events:
        if event == "enter":
            count += 1
        elif event == "exit":
            count -= 1
    
    return count

events = ["enter", "enter", "exit", "enter"]
result = count_people(events)
print(result)

events2 = ["enter", "exit", "enter", "enter", "exit"]
result2 = count_people(events2)
print(result2)