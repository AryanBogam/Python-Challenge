def check_breakpoint(breakpoints_list, line_number):
    """
    Checks if a specific line number has a breakpoint
    """
    if line_number in breakpoints_list:
        return True
    else:
        return False

def display_breakpoint_status(breakpoints_list, line_number):
    """
    Shows a nice message about breakpoint status
    """
    if check_breakpoint(breakpoints_list, line_number):
        print(f"Line {line_number}: Has breakpoint 🔴")
    else:
        print(f"Line {line_number}: No breakpoint")

breakpoints = [5, 12, 20]
line_to_check = 12

has_breakpoint = check_breakpoint(breakpoints, line_to_check)
print(f"Does line {line_to_check} have a breakpoint? {has_breakpoint}")

print("\nBreakpoint Status:")
print("==================")
display_breakpoint_status(breakpoints, 5)
display_breakpoint_status(breakpoints, 10)
display_breakpoint_status(breakpoints, 12)
display_breakpoint_status(breakpoints, 15)
display_breakpoint_status(breakpoints, 20)

print(f"\nAll breakpoints are on lines: {breakpoints}")

more_breakpoints = [1, 3, 7, 15, 25, 30]
print(f"\nTesting with breakpoints on lines: {more_breakpoints}")
display_breakpoint_status(more_breakpoints, 7)
display_breakpoint_status(more_breakpoints, 8)
display_breakpoint_status(more_breakpoints, 25)