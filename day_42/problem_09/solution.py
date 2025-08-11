def count_lines(file_content):
    """
    Counts total lines and non-empty lines in file content
    """
    lines = file_content.split('\n')
    total_lines = len(lines)
    non_empty_lines = 0
    
    for line in lines:
        if line.strip() != "":
            non_empty_lines += 1
    
    return total_lines, non_empty_lines

def display_line_count(file_content, description="File"):
    """
    Shows line count information nicely
    """
    total, non_empty = count_lines(file_content)
    print(f"{description}:")
    print(f"  Total lines: {total}")
    print(f"  Non-empty lines: {non_empty}")
    print(f"  Empty lines: {total - non_empty}")

file_content = "print('Hello')\n\nprint('World')"
total, non_empty = count_lines(file_content)
print(f"Example: Total = {total}, Non-empty = {non_empty}")

print(f"\nFile content:")
print(repr(file_content))
print(f"\nFile content (formatted):")
print(file_content)

print("\n" + "="*40)

test1 = "line1\nline2\nline3"
display_line_count(test1, "Test 1 (no empty lines)")

test2 = "line1\n\nline2\n\n\nline3"
display_line_count(test2, "Test 2 (with empty lines)")

test3 = "print('Hello')\n# This is a comment\n\nprint('World')\n"
display_line_count(test3, "Test 3 (Python code)")

test4 = ""
display_line_count(test4, "Test 4 (empty file)")