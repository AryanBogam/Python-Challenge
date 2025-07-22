while True:
    reply = input("Tower: Clear to land? ").strip().lower()
    if reply == "roger":
        print("Tower: Landing confirmed.")
        break
    else:
        print("Tower: Say again...")