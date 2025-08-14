def close_tabs(open_tabs, tabs_to_close):
    remaining_tabs = []
    for tab in open_tabs:
        if tab not in tabs_to_close:
            remaining_tabs.append(tab)
    return remaining_tabs

open_tabs = ["google.com", "youtube.com", "github.com"]
tabs_to_close = ["youtube.com"]

print(f"Open tabs: {open_tabs}")
print(f"Closing: {tabs_to_close}")

remaining = close_tabs(open_tabs, tabs_to_close)
print(f"Remaining tabs: {remaining}")

test_cases = [
    (["google.com", "youtube.com", "github.com"], ["youtube.com"]),
    (["tab1.com", "tab2.com", "tab3.com"], ["tab1.com", "tab3.com"]),
    (["only-tab.com"], ["only-tab.com"]),
    (["keep.com", "close.com"], ["not-open.com"])
]

for open_tabs, close_tabs in test_cases:
    remaining = close_tabs(open_tabs, close_tabs)
    print(f"\nOpen: {open_tabs}")
    print(f"Close: {close_tabs}")
    print(f"Remaining: {remaining}")

def close_tabs_with_count(open_tabs, tabs_to_close):
    remaining_tabs = []
    closed_count = 0
    
    for tab in open_tabs:
        if tab in tabs_to_close:
            closed_count += 1
        else:
            remaining_tabs.append(tab)
    
    print(f"Closed {closed_count} tabs")
    return remaining_tabs

print(f"\nWith close count:")
tabs = ["site1.com", "site2.com", "site3.com"]
to_close = ["site1.com", "site3.com"]
remaining = close_tabs_with_count(tabs, to_close)
print(f"Remaining: {remaining}")