def count_file_types(file_list):
    """
    Takes a list of file names and counts each file extension
    """
    file_count = {}
    for file_name in file_list:
        if '.' in file_name:
            extension = file_name[file_name.rfind('.'):]
            if extension in file_count:
                file_count[extension] += 1
            else:
                file_count[extension] = 1
    
    return file_count

files = ["main.py", "test.py", "index.html"]
result = count_file_types(files)
print(f"File types: {result}")

test1 = ["main.py", "test.py", "index.html", "styles.css", "app.js", "data.json"]
result1 = count_file_types(test1)
print(f"Test 1: {result1}")

test2 = ["README", "LICENSE"]
result2 = count_file_types(test2)
print(f"Test 2: {result2}")