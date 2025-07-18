def classify_file(filename):
    ext = filename.lower().split(".")[-1]
    if ext in ["doc", "docx"]:
        return "Word Document"
    elif ext in ["xls", "xlsx"]:
        return "Excel Spreadsheet"
    elif ext in ["ppt", "pptx"]:
        return "PowerPoint Presentation"
    else:
        return "Unknown Format"

print(classify_file("budget.xlsx"))
