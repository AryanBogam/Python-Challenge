def switch_theme(current_theme):
    """
    Switches between Light and Dark themes
    """
    if current_theme == "Light":
        return "Dark"
    elif current_theme == "Dark":
        return "Light"
    else:
        return "Light"

def display_theme_change(old_theme, new_theme):
    """
    Shows theme change with nice formatting
    """
    if new_theme == "Dark":
        print(f"Switched from {old_theme} to {new_theme}")
    else:
        print(f"Switched from {old_theme} to {new_theme}")

current_theme = "Light"
print(f"Current theme: {current_theme}")

new_theme = switch_theme(current_theme)
display_theme_change(current_theme, new_theme)

current_theme = new_theme
newer_theme = switch_theme(current_theme)
display_theme_change(current_theme, newer_theme)

current_theme = newer_theme
final_theme = switch_theme(current_theme)
display_theme_change(current_theme, final_theme)

print("\n" + "="*30)
print("Testing multiple switches:")

theme = "Light"
print(f"Starting theme: {theme}")

for i in range(5):
    old_theme = theme
    theme = switch_theme(theme)
    print(f"Switch {i+1}: {old_theme} → {theme}")

print("\nTesting with invalid theme:")
invalid_theme = "Blue"
result = switch_theme(invalid_theme)
print(f"'{invalid_theme}' → '{result}' (defaults to Light)")