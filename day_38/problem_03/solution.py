def is_story_expired(hours_ago):
    if hours_ago > 24:
        return "Expired"
    else:
        return "Still Active"

result = is_story_expired(26)
print(result)

result2 = is_story_expired(12)
print(result2)

result3 = is_story_expired(24)
print(result3)