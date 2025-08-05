def validate_upload(file_size):
    if file_size > 2048:
        return "Upload Failed: File too big"
    else:
        return "Upload Successful"

file_size = 2500
result = validate_upload(file_size)
print(result)

file_size2 = 1500
result2 = validate_upload(file_size2)
print(result2)