def streak_saver_status(has_saver):
    if has_saver == True:
        return "Streak Saver Active"
    else:
        return "No Streak Saver"

result = streak_saver_status(True)
print(result)

result2 = streak_saver_status(False)
print(result2)