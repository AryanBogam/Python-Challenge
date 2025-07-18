cloud_files = {"resume.pdf", "project.docx"}

def sync_file(file_name):
    if file_name in cloud_files:
        return f"{file_name} already synced to OneDrive."
    else:
        cloud_files.add(file_name)
        return f"{file_name} uploaded to OneDrive."

print(sync_file("notes.txt"))
print(sync_file("resume.pdf"))
