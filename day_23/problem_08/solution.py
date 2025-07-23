student_ids = {
    "Aryan": 101,
    "Riya": 102,
    "Om": 103
}

swapped = {}

for name, id in student_ids.items():
    swapped[id] = name

print(swapped)