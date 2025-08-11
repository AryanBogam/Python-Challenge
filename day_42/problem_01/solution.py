def count_open_files(file_list):
    """
    Takes a list of file names and returns how many files are open
    """
    return len(file_list)

files = ["main.py", "index.html", "styles.css"]
result = count_open_files(files)
print(f"Number of open files: {result}")

test1 = ["main.py"]
test2 = ["main.py", "index.html", "styles.css", "app.js", "test.py"]
test3 = []

print(f"Test 1: {count_open_files(test1)} files")
print(f"Test 2: {count_open_files(test2)} files") 
print(f"Test 3: {count_open_files(test3)} files")