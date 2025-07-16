def verify_image_files(file_list):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    accepted = []
    
    for filename in file_list:
        if '.' in filename:
            ext = '.' + filename.split('.')[-1].lower()
            if ext in valid_extensions:
                accepted.append(filename)
    
    return accepted

files = ["photo.jpg", "document.pdf", "image.png", "video.mp4"]
result = verify_image_files(files)
print(result)