def calculate_stream_length(start_hour, end_hour):
    duration = end_hour - start_hour
    return f"Stream lasted {duration} hours"

result = calculate_stream_length(14, 18)
print(result)

result2 = calculate_stream_length(19, 22)
print(result2)

result3 = calculate_stream_length(10, 16)
print(result3)