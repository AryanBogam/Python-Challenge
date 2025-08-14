def clear_history(history):
    return []

history = ["google.com", "youtube.com"]
print(f"Before clearing: {history}")

cleared_history = clear_history(history)
print(f"After clearing: {cleared_history}")

test_histories = [
    ["google.com", "youtube.com", "github.com"],
    ["facebook.com", "twitter.com"],
    []
]

for hist in test_histories:
    print(f"\nOriginal history: {hist}")
    cleared = clear_history(hist)
    print(f"Cleared history: {cleared}")

def clear_history_with_message(history):
    original_count = len(history)
    cleared = []
    print(f"Cleared {original_count} items from history")
    return cleared

print("\nWith confirmation message:")
history = ["site1.com", "site2.com", "site3.com"]
cleared = clear_history_with_message(history)
print(f"Result: {cleared}")