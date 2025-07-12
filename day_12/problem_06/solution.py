def is_isomorphic(s, t):
    mapping_s, mapping_t = {}, {}
    for a, b in zip(s, t):
        if mapping_s.get(a, b) != b or mapping_t.get(b, a) != a:
            return False
        mapping_s[a] = b
        mapping_t[b] = a
    return True

print(is_isomorphic("egg", "add"))  
print(is_isomorphic("foo", "bar"))  
