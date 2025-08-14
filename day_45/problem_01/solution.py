def count_total_tabs(current_tabs, new_tabs):
    total_tabs = current_tabs + new_tabs
    return total_tabs

current_tabs = 5
new_tabs = 3
total = count_total_tabs(current_tabs, new_tabs)
print(f"Current tabs: {current_tabs}")
print(f"New tabs: {new_tabs}")
print(f"Total tabs: {total}")

test_cases = [
    (5, 3),
    (10, 2),
    (0, 5),
    (7, 0)
]

for current, new in test_cases:
    total = count_total_tabs(current, new)
    print(f"{current} + {new} = {total} tabs")