video_length = 300
jump_to = 120

if jump_to < 0 or jump_to > video_length:
    print("Invalid timestamp")
else:
    print("Now at " + str(jump_to) + "s")