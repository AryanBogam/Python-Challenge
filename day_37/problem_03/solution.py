def can_watch(age):
    if age >= 18:
        return "Allowed"
    else:
        return "Blocked"

age = 16
result = can_watch(age)
print(result)

result2 = can_watch(20)
print(result2)

result3 = can_watch(18)
print(result3)