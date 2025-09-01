def check_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    double_str = str1 + str1
    return str2 in double_str

str1 = "ABCD"
str2 = "CDAB"
result = check_rotation(str1, str2)
print(result)