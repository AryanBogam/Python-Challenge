user_input = input("Expression: ").strip()

x, y, z = user_input.split(" ")
x = float(x)
z = float(z)

if "+" in user_input:
    print(x + z)
elif "-" in user_input:
    print(x - z)
elif "*" in user_input:
    print(x * z)
elif "/" in user_input:
    print(x // z)