def check_extension_installed(extensions_list, extension_name):
    """
    Checks if a specific extension is installed
    """
    if extension_name in extensions_list:
        return True
    else:
        return False

def display_extension_status(extensions_list, extension_name):
    """
    Shows a nice message about extension status
    """
    if check_extension_installed(extensions_list, extension_name):
        print(f'"{extension_name}" is installed')
    else:
        print(f'"{extension_name}" is NOT installed')

installed_extensions = ["Python", "Prettier", "Live Server"]
extension_to_check = "Python"

is_installed = check_extension_installed(installed_extensions, extension_to_check)
print(f'Is "{extension_to_check}" installed? {is_installed}')

display_extension_status(installed_extensions, "Python")
display_extension_status(installed_extensions, "Prettier")
display_extension_status(installed_extensions, "GitLens")
display_extension_status(installed_extensions, "Live Server")

more_extensions = ["Python", "JavaScript", "HTML", "CSS", "Git"]
print("\nChecking more extensions:")
display_extension_status(more_extensions, "Python")
display_extension_status(more_extensions, "Java")
display_extension_status(more_extensions, "CSS")