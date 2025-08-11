import time
def check_auto_save(last_save_time, auto_save_limit_seconds):
    """
    Checks if auto-save should happen based on time passed
    """
    current_time = time.time()
    time_passed = current_time - last_save_time
    if time_passed >= auto_save_limit_seconds:
        print("Auto-saved!")
        return current_time
    else:
        remaining_time = auto_save_limit_seconds - time_passed
        print(f"No auto-save needed. {remaining_time:.1f} seconds remaining")
        return last_save_time

print("Auto-Save Simulation:")
print("===================")

last_save = time.time()
auto_save_limit = 3

print("Initial save...")
print(f"Auto-save will happen after {auto_save_limit} seconds")

print("\nChecking after 0 seconds:")
last_save = check_auto_save(last_save, auto_save_limit)

print(f"\nWaiting 2 seconds...")
time.sleep(2)
print("Checking after 2 seconds:")
last_save = check_auto_save(last_save, auto_save_limit)
print(f"\nWaiting 2 more seconds...")
time.sleep(2)
print("Checking after 4 seconds total:")
last_save = check_auto_save(last_save, auto_save_limit)