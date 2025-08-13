def check_storage_capacity(current_usage, new_file_size, limit=500):
    total_after_upload = current_usage + new_file_size
    
    if total_after_upload > limit:
        return "Storage limit exceeded"
    else:
        return "Storage capacity available"

current_usage = 450
new_file_size = 60
result = check_storage_capacity(current_usage, new_file_size)
print(f"Current: {current_usage}GB, Adding: {new_file_size}GB")
print(f"Result: {result}")

test_cases = [
    (400, 50),
    (450, 60),
    (300, 100),
    (480, 30)
]

for current, new_size in test_cases:
    result = check_storage_capacity(current, new_size)
    total = current + new_size
    print(f"Current: {current}GB + New: {new_size}GB = {total}GB -> {result}")

def get_remaining_capacity(current_usage, limit=500):
    return limit - current_usage

remaining = get_remaining_capacity(450)
print(f"\nRemaining capacity: {remaining}GB")