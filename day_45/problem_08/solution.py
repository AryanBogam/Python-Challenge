def switch_theme(theme):
    if theme == "light":
        return "Switching to Light Mode"
    elif theme == "dark":
        return "Switching to Dark Mode"
    else:
        return "Unknown theme"

theme = "dark"
message = switch_theme(theme)
print(message)

themes = ["light", "dark", "blue"]

for theme_name in themes:
    result = switch_theme(theme_name)
    print(f'Theme "{theme_name}": {result}')

def toggle_theme(current_theme):
    if current_theme == "light":
        new_theme = "dark"
    elif current_theme == "dark":
        new_theme = "light"
    else:
        new_theme = "light"
    
    message = switch_theme(new_theme)
    return new_theme, message

print(f"\nToggling themes:")
current = "light"
for i in range(4):
    current, message = toggle_theme(current)
    print(f"Step {i+1}: {message}")

def print_theme_switch(theme):
    if theme == "light":
        print("Switching to Light Mode")
    elif theme == "dark":
        print("Switching to Dark Mode")
    else:
        print("Unknown theme")

print(f"\nDirect print version:")
print_theme_switch("light")
print_theme_switch("dark")