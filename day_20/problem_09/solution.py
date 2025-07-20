def privacy_toggle_tracker(toggles):
    count = {}
    for setting in toggles:
        count[setting] = count.get(setting, 0) + 1

    for setting, times in count.items():
        if times > 5:
            print(f"'{setting}' toggled {times} times. Suggest showing Help Guide.")
        else:
            print(f"'{setting}' toggled {times} times. No issue.")

toggle_log = ["location", "camera", "location", "location", "location", "location", "location"]
privacy_toggle_tracker(toggle_log)
