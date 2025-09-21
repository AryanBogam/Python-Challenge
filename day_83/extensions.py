GIF_EXTENSION = ".gif"
JPG_EXTENSION = ".jpg"
JPEG_EXTENSION = ".jpeg"
PNG_EXTENSION = ".png"
PDF_EXTENSION = ".pdf"
TXT_EXTENSION = ".txt"
ZIP_EXTENSION = ".zip"

user_input = input("File name: ").lower().strip()

if GIF_EXTENSION in user_input:
    print("image/gif")
elif JPG_EXTENSION in user_input:
    print("image/jpeg")
elif JPEG_EXTENSION in user_input:
    print("image/jpeg")
elif PNG_EXTENSION in user_input:
    print("image/png")
elif PDF_EXTENSION in user_input:
    print("application/pdf")
elif TXT_EXTENSION in user_input:
    print("text/plain")
elif ZIP_EXTENSION in user_input:
    print("application/zip")
else:
    print("application/octet-stream")