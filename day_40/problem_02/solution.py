def check_stream_status(is_live):
    if is_live == True:
        return "Stream is LIVE!"
    else:
        return "Stream is offline"

is_live = True
result = check_stream_status(is_live)
print(result)

result2 = check_stream_status(False)
print(result2)

result3 = check_stream_status(True)
print(result3)