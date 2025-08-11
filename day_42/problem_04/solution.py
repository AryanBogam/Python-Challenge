def search_files(file_list, keyword):
    """
    Searches for files containing a keyword in their name
    """
    matching_files = []
    for file_name in file_list:
        if keyword in file_name:
            matching_files.append(file_name)
    return matching_files

files = ["main.py", "test.py", "main_test.js"]
keyword = "main"
result = search_files(files, keyword)
print(f'Files containing "{keyword}": {result}')

test_files = ["main.py", "test.py", "main_test.js", "app.js", "main_config.json", "helper.py"]

result1 = search_files(test_files, "main")
print(f'Files with "main": {result1}')

result2 = search_files(test_files, "test")
print(f'Files with "test": {result2}')

result3 = search_files(test_files, ".py")
print(f'Python files: {result3}')

result4 = search_files(test_files, "xyz")
print(f'Files with "xyz": {result4}')