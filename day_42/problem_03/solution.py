def manage_recent_files(recent_files, new_file, limit):
    """
    Manages a list of recent files with a maximum limit
    When limit is reached, removes the oldest file
    """
    recent_files.append(new_file)
    if len(recent_files) > limit:
        recent_files.pop(0)
    return recent_files

recent = []
limit = 3

recent = manage_recent_files(recent, "main.py", limit)
print(f"After opening main.py: {recent}")

recent = manage_recent_files(recent, "index.html", limit)
print(f"After opening index.html: {recent}")

recent = manage_recent_files(recent, "styles.css", limit)
print(f"After opening styles.css: {recent}")

recent = manage_recent_files(recent, "app.py", limit)
print(f"After opening app.py: {recent}")

recent = manage_recent_files(recent, "test.js", limit)
print(f"After opening test.js: {recent}")