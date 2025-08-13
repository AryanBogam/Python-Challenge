def check_blob_name(file_name):
    """
    Checks if blob name is valid:
    - Only lowercase letters, numbers, and hyphens
    - Must start and end with letter or number
    """
    if not (file_name[0].isalnum() and file_name[-1].isalnum()):
        return "Invalid blob name"
    
    for char in file_name:
        if not (char.islower() or char.isdigit() or char == '-'):
            return "Invalid blob name"
    
    return "Valid blob name"

test_names = [
    "my-file-1",
    "MyFile",
    "file_name",
    "-invalid",
    "valid-name-2",
    "test123"
]

for name in test_names:
    result = check_blob_name(name)
    print(f'"{name}": {result}')