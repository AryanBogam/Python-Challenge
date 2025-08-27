responses = []

print("What programming language do you like most?")
print("Options: Python, Java, JavaScript, C++, Other")

while True:
    response = input("Enter your choice (or 'stop' to finish): ")
    if response == "stop":
        break
    responses.append(response)

print("\nPoll Results:")
for response in set(responses):
    count = responses.count(response)
    print(response + ":", count, "votes")

print("Total responses:", len(responses))