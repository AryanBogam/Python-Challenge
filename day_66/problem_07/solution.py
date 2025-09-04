def rotate_string(s, k):
    n = len(s)
    k = k % n
    return s[k:] + s[:k]

s = "hello"
k = 2
result = rotate_string(s, k)
print(result)